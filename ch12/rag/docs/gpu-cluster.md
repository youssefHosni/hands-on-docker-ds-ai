# GPU Cluster

## Booking GPUs

GPUs are booked in the #gpu-booking channel before a job starts. Write the number of GPUs, the expected
run time and the project name. Bookings are first come, first served.

## Limits

One person can use at most 4 GPUs at the same time. A single job can run for at most 48 hours; longer
trainings must save checkpoints and be restarted. Jobs that run longer are stopped without warning.

## Queues

Short jobs (under 2 hours) go to the `quick` queue. Everything else goes to the `long` queue. The
`quick` queue is reserved for interactive work between 09:00 and 17:00.
