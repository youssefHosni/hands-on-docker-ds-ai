# Chapter 3 exercise: answer

The files in this folder are `ch03/` with one line of `train.py` changed (line 7):

```python
y = np.array([3, 6, 9, 12, 15])
```

Rebuilding (run 1 Nov 2026, recorded in `outputs/ch03-exercise.txt`):

```
[+] Building 0.7s (11/11) FINISHED
 => CACHED [2/6] WORKDIR /app
 => CACHED [3/6] COPY requirements.txt .
 => CACHED [4/6] RUN pip install --no-cache-dir -r requirements.txt
 => [5/6] COPY . .
 => [6/6] RUN python train.py                                              0.6s
```

And the new model predicts y = 3x:

```
$ curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"input": [6, 7, 8]}'
{"prediction":[18.000000000000004,21.000000000000004,24.000000000000004]}
```

- **From the cache:** steps 2 to 4. `requirements.txt` didn't change, so the packages weren't
  installed again.
- **Ran again:** `COPY . .` and `RUN python train.py`.
- **Why training ran again:** `train.py` changed, so the files copied by `COPY . .` changed, and that
  step's cache was invalid. Once one step runs again, every step after it runs again too, even if
  its own line in the Dockerfile is the same. That's exactly what we want here: new training data,
  new model. The whole build took 0.7 seconds instead of 15.
