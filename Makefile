SHELL:=/bin/bash

include .env

#
# Execute these commands insice the docker environment
# e.g. commands that rely on installed libraries and etc.
#
.PHONY: lint test-unit test-integration test-local-integration
lint test-unit test-integration test-local-integration:
	docker-compose run --rm api ./tools.sh $(MAKECMDGOALS) $(MAKEFLAGS)

#
# Execute these commands on the host machine
# e.g. commands that themselves use docker
#
.PHONY: deploy set-service-host destory build tag push dynamo-setup s3-setup delete-image login ssm-setup
deploy set-service-host destory build tag push dynamo-setup s3-setup delete-image login ssm-setup:
	./tools.sh $(MAKECMDGOALS) $(MAKEFLAGS)
