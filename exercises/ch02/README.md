# Chapter 2 exercise: answer

Run 1 Nov 2026, recorded in `outputs/ch02-exercise.txt`.

```bash
docker run --name iris-run iris-classifier:1.0     # prints Accuracy: 1.0, then the container stops
docker ps -a --filter name=iris-run                # the stopped container: Exited (0)
docker logs iris-run                               # Accuracy: 1.0, without running it again
docker rm iris-run                                 # 1. the container
docker rmi iris-classifier:1.0                     # 2. then the image
```

**Order:** the container first, then the image. The other order fails, because a stopped container
still uses its image:

```
$ docker rmi iris-classifier:1.0
Error response from daemon: conflict: unable to delete iris-classifier:1.0 (must be forced) - container afc16ab663f8 is using its referenced image 84428fbd3b28
```

`docker rmi -f` would "work", but it only removes the name `iris-classifier:1.0`: the image stays on
disk as long as the `iris-run` container exists.

To get the image back, build it again in `ch01/` with `docker build -t iris-classifier:1.0 .`
