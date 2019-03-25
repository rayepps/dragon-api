SHELL:=/bin/bash

include .env

KEY = $(shell aws --profile default configure get aws_access_key_id)
SECRET = $(shell aws --profile default configure get aws_secret_access_key)
TOKEN = $(shell aws --profile default configure get aws_session_token)
REGION = $(shell aws --profile default configure get region)
export AWS_ACCESS_KEY_ID = ${KEY}
export AWS_SECRET_ACCESS_KEY = ${SECRET}
export AWS_SESSION_TOKEN = ${TOKEN}
export AWS_DEFAULT_REGION = ${REGION}


.PHONY: lint test-unit deploy remove dynamo-local-migrate
lint test-unit deploy remove dynamo-local-migrate:
	docker-compose run --rm app make -f Makefile.targets $(MAKECMDGOALS) $(MAKEFLAGS)
