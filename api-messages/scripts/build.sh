#!/usr/bin/env bash

TAG=$(cat docker-tag | xargs)

REGISTRY_TAG="ragibkl/example-api-messages:$TAG"
echo "REGISTRY_TAG=$REGISTRY_TAG"

docker build --pull -t $REGISTRY_TAG -f ./Dockerfile .
docker push $REGISTRY_TAG
