"""Code an agent wrote and wants to run. What can it reach?"""
import threading
import time
import urllib.request


def attempt(name, action):
    try:
        print(f"{name}: yes ({action()})")
    except BaseException as e:
        print(f"{name}: no ({type(e).__name__})")


def internet():
    return urllib.request.urlopen("https://pypi.org/simple/", timeout=5).status


def write_app():
    return open("/usr/local/lib/note.txt", "w").write("changed")


def start_threads():
    threads = [threading.Thread(target=time.sleep, args=(5,)) for _ in range(500)]
    for t in threads:
        t.start()
    return f"{len(threads)} threads"


attempt("Reach the internet", internet)
attempt("Change files in the image", write_app)
attempt("Start 500 threads", start_threads)
attempt("Use 1 GB of memory", lambda: len(bytearray(1_000_000_000)))
