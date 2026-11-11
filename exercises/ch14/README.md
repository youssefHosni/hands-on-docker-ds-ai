# Chapter 14 exercise: make the test catch more

**Task.** Add a check to `ci/test.sh`: a bad request must get a 422. Then break the model on purpose, and see
the test stop the pipeline.

**Answer.** `test.sh` here is `ch14/ci/test.sh` with the new check. From `ch14/`:

```bash
cp ../exercises/ch14/test.sh ci/test.sh
docker build -q -t ml-app:ci .
ci/test.sh ml-app:ci; echo "exit code: $?"
```

The test passes, with `Bad request: 422`. To break the model, change `y` in `train.py` to
`[3, 6, 9, 12, 15]` and build again: the API still starts and still answers, but with 18, so the test prints
`FAILED: expected 12.0` and exits with 1. In the workflow, a step that exits with anything but 0 stops the job,
so the steps that sign in and push never run, and the wrong model never reaches the registry. A health
check alone wouldn't have caught this: the server was healthy, and only wrong.
Recorded run: `outputs/ch14-exercise.txt`. Remember to undo both changes.
