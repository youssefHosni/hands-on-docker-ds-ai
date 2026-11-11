# Chapter 1 exercise: answer

The files in this folder are `ch01/` with the model changed to a decision tree
(`iris_classification.py`, lines 4, 15 and 16).

Building again (run 30 Oct 2026, recorded in `outputs/ch01-exercise.txt`):

```
[+] Building 0.1s (10/10) FINISHED
 => CACHED [2/5] WORKDIR /src
 => CACHED [3/5] COPY requirements.txt .
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt
 => [5/5] COPY . .
```

- **Reused from the cache:** steps 2 to 4, marked `CACHED`. Only `COPY . .` ran again.
- **Time:** 0.1 seconds, against 13.2 seconds for the first build.
- **Why the packages weren't installed again:** Docker reuses a step when the step and
  everything before it are unchanged. `requirements.txt` didn't change, so `COPY requirements.txt .`
  and the `pip install` after it were the same as last time. The code changed, so `COPY . .` ran
  again. This is why the Dockerfile copies `requirements.txt` on its own, before the rest of the
  code. If it copied everything first, every code change would reinstall every package.

Running the new image prints `Accuracy: 1.0`: the decision tree also gets all 30 test flowers right.
