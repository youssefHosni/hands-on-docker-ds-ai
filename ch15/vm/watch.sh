#!/bin/sh
# Calls the API every 0.2 seconds until you stop it, and prints one status code per call.
while true; do
  curl -sk -o /dev/null -m 2 -w "%{http_code}\n" https://localhost/health
  sleep 0.2
done
