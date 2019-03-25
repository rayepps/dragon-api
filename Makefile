SHELL:=/bin/bash

include .env

KEY = $(shell aws --profile default configure get aws_access_key_id)
SECRET = $(shell aws --profile default configure get aws_secret_access_key)
TOKEN = $(shell aws --profile default configure get aws_session_token)
REGION = $(shell aws --profile default configure get region)
VERSION = $(shell cat ./version.cfg)

export AWS_ACCOUNT_ID = 957774660254
export AWS_ACCESS_KEY_ID = ${KEY}
export AWS_SECRET_ACCESS_KEY = ${SECRET}
export AWS_SESSION_TOKEN = ${TOKEN}
export AWS_DEFAULT_REGION = ${REGION}
export IMAGE_VERSION = ${VERSION}

.PHONY: lint test-unit
lint test-unit:
	docker-compose run --rm api make -f Makefile.targets $(MAKECMDGOALS) $(MAKEFLAGS)

.PHONY: login
login:
	$(aws ecr get-login --no-include-email --region us-west-2)

.PHONY: build
build:
	docker build -t dragon-api:${IMAGE_VERSION} .

.PHONY: tag
tag:
	docker tag dragon-api:${IMAGE_VERSION} ${AWS_ACCOUNT_ID}.dkr.ecr.us-west-2.amazonaws.com/dragon-api:${IMAGE_VERSION}

.PHONY: push
push: login
	docker push ${AWS_ACCOUNT_ID}.dkr.ecr.us-west-2.amazonaws.com/dragon-api:${IMAGE_VERSION}
