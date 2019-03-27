#!/usr/bin/env bash

deploy() {
  make build version=$BUILD_ID
  make tag version=$BUILD_ID
  make push version=$BUILD_ID
  make deploy version=$BUILD_ID
}

destroy() {
  make destroy version=$BUILD_ID
  make delete-image version=$BUILD_ID
}

set_deployed_stack_url() {
  make set-service-host version=$BUILD_ID
}

integration_test() {
  make test-integration host=$STACK_HOST
}

make lint;
status=$?
if [ $status != 0 ]; then exit $status; fi

make test-unit;
status=$?
if [ $status != 0 ]; then exit $status; fi

if [ "$TRAVIS_EVENT_TYPE" == "pull_request" ]; then
    export BUILD_ID=travis_$(echo $TRAVIS_PULL_REQUEST_SHA | awk '{print substr($0,1,8)}');
    if deploy; then
      if set_deployed_stack_url; then
        if integration_test; then
          destroy;
          exit 0
        fi
      fi
    fi
    destroy;
    exit 1
else
