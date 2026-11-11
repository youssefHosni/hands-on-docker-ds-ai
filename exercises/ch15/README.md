# Chapter 15 exercise: what the probes were doing

**Task.** Roll out the broken image (`ml-api:1.1.0`, which has lost its model) on a Deployment with no probes, and
compare it with what happened in the chapter.

**Answer.** `deployment-no-probes.yaml` here is `ch15/k8s/deployment.yaml` without `readinessProbe` and
`livenessProbe`. On a `kind` cluster with both images loaded and `service.yaml` applied:

```bash
kubectl apply -f deployment-no-probes.yaml
kubectl set image deployment/ml-api api=ml-api:1.1.0
kubectl rollout status deployment/ml-api --timeout=60s
kubectl run client --rm -i --quiet --restart=Never --image=curlimages/curl:8.17.0 -- \
  sh -c "sleep 3; for i in 1 2 3 4 5 6 7 8 9 10; do curl -s -o /dev/null -w \"%{http_code} \" http://ml-api/health; done; echo"
```

`rollout status` says `deployment "ml-api" successfully rolled out`, and the Service answers `503` ten times out of
ten. With no probe, a Pod counts as ready as soon as its process is running. So Kubernetes replaced both good Pods
with broken ones in a few seconds and reported success. A real `/predict` call answers
`{"detail":"Model not loaded"}`. In the chapter, with probes, the same image stopped at one new Pod, and the Service
answered `200` ten times out of ten.

So the advice to a colleague is: always add a `readinessProbe` (it stops a bad release and keeps traffic away from
a Pod that can't answer), and it has to call an endpoint that really checks the model, not one that only says the
process is alive. Add a `livenessProbe` too, so a stuck container gets restarted. A probe is only as good as its
endpoint: a `/health` that always answers 200 would have let this release through as well.

Recorded run: `outputs/ch15-exercise.txt`.
