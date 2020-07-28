#!/bin/bash

VERSION_BASE="1.0"

BUILDNUMBER=$(date "+%j%H%M%S")
VERSION="${VERSION_BASE}.${BUILDNUMBER}"

if [ -n "$DOCKER_TAG" ] && [ "$DOCKER_TAG" != "latest" ]; then
    VERSION="$DOCKER_TAG"
fi

echo "$VERSION"
