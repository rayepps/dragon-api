#!/bin/bash

# Parse key value arguemnts into bash variables
# i.e. host=http://aplace.com
for argument; do
    if [[ $argument == *=* ]]; then
      key=${argument%%=*}
      val=${argument#*=}
      declare "${key}"=${val}
    fi
done


#
# Setup aws creds
#

export AWS_ACCOUNT_ID="957774660254"
export AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
export AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)
export AWS_SESSION_TOKEN=$(aws --profile default configure get aws_session_token)
export AWS_DEFAULT_REGION=$(aws --profile default configure get region)


#
# Helper
#

require() {
  varname=$1
  if [[ -z "${!varname}" ]]; then
    echo "This tool command requires the $varname argument"
    exit 1
  fi
}


#
# Commands
#

lint() {
	pylint ./src
}

test-unit() {
	py.test --color=yes --cov-report html --cov-report term --cov=src test/unit --cov-fail-under=1
}

test-integration() {
  require "host"
	export INTEGRATION_TEST_HOST=$host
  py.test --color=yes --cov-report html --cov-report term --cov=src test/integration
}

test-local-integration() {
  export INTEGRATION_TEST_HOST="http://host.docker.internal:5000"
  py.test --color=yes --cov-report html --cov-report term --cov=src test/integration
}

dynamo-setup() {
	python -u util/setup_dynamo.py
}

s3-setup() {
	python -u util/setup_s3.py
}

ssm-setup() {
  python -u util/setup_ssm.py
}

set-service-host() {
  require "version"
  stack_description=$(aws cloudformation describe-stacks --stack-name dragon-api-$version)
  stack_host=$(jq '.Stacks[0].Outputs[] | select(.OutputKey == "ServiceUrl").OutputValue' | $stack_description)
  export STACK_HOST=$stack_host
}

deploy() {
  require "version"
	parameters=$(python util/build_deploy_command_parameters.py --version $version)
	aws cloudformation deploy --template-file cloudformation/service.yml --stack-name dragon-api-$version --parameter-overrides $parameters
}

destroy() {
  require "version"
	aws cloudformation delete-stack --stack-name dragon-api-$version
}

build() {
  require "version"
	docker build -t dragon-api:${version} .
}

tag() {
  require "version"
	docker tag dragon-api:${version} ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/dragon-api:${version}
}

push() {
  require "version"
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/dragon-api:${version}
}

login() {
  aws ecr get-login --registry-ids $AWS_ACCOUNT_ID --no-include-email --region us-west-2 | sed 's|https://||' | sh
}

delete-image() {
  require "version"
  aws ecr batch-delete-image --repository-name dragon-api --image-ids imageTag=$version
}


# Execute whatever command was passed
# Check if the function exists (bash specific)
if declare -f "$1" > /dev/null; then
  "$1" # call arguments verbatim
else
  # Show a helpful error
  echo "'$1' is not a known function name" >&2
  exit 1
fi
