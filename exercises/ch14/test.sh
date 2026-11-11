#!/bin/sh
# Starts the image, then checks that the API answers correctly. Usage: ci/test.sh IMAGE
set -eu
image=$1
name=ci-test-$$

docker run -d --name "$name" -p 127.0.0.1:18000:8000 "$image" >/dev/null
trap 'docker rm -f "$name" >/dev/null' EXIT

# Wait for the server: up to 30 seconds
for _ in $(seq 30); do
  curl -sf http://127.0.0.1:18000/ >/dev/null && break
  sleep 1
done

answer=$(curl -sf http://127.0.0.1:18000/predict -H "Content-Type: application/json" \
  -d '{"input": [6]}')
echo "Answer: $answer"

# The model learned y = 2x, so 6 must give 12
echo "$answer" | grep -q '12\.0' || { echo "FAILED: expected 12.0"; exit 1; }

# A bad request must be refused, not crash the server
status=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:18000/predict \
  -H "Content-Type: application/json" -d '{"input": "six"}')
echo "Bad request: $status"
[ "$status" = 422 ] || { echo "FAILED: expected 422"; exit 1; }
echo "PASSED"
