# Model Deployment

## Before a Release

Every model release needs a model card and an evaluation report in the project repository. Two
reviewers must approve the release, and at least one of them must be from outside the project team.

## Canary Releases

A new model first serves 10% of the traffic for 24 hours. If its error rate stays below the current
model's, it gets all of the traffic. Releases never start on a Friday.

## Rollbacks

Anyone on the team can roll back a model without asking. Roll back first, then write a short report in
the #ml-incidents channel within one working day.
