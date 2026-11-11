#!/bin/sh
# Fails if the image has a critical vulnerability with a fix available. Usage: ci/scan.sh IMAGE
set -eu
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:0.76.1 image --quiet --scanners vuln --table-mode detailed --severity CRITICAL --ignore-unfixed --exit-code 1 "$1"
