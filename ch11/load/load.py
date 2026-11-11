import json
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from statistics import quantiles

# python load.py <url> <clients> <requests>: send <requests> requests, <clients> at a time
url, clients, total = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
body = json.dumps({"texts": ["Docker made our model deployment painless."] * 16}).encode()


def send(_):
    request = urllib.request.Request(url, body, {"Content-Type": "application/json"})
    start = time.perf_counter()
    try:
        urllib.request.urlopen(request, timeout=30).read()
        return "ok", time.perf_counter() - start
    except urllib.error.HTTPError as error:
        return error.code, time.perf_counter() - start


start = time.perf_counter()
with ThreadPoolExecutor(clients) as pool:
    results = list(pool.map(send, range(total)))
elapsed = time.perf_counter() - start

ok = sorted(seconds for status, seconds in results if status == "ok")
errors = [status for status, _ in results if status != "ok"]
print(f"{len(ok)} ok, {len(errors)} errors {sorted(set(errors))}, {len(ok) / elapsed:.1f} requests/s")
if len(ok) > 1:
    p50, p95 = quantiles(ok, n=20)[9], quantiles(ok, n=20)[18]
    print(f"latency: median {p50:.2f} s, 95th percentile {p95:.2f} s")
