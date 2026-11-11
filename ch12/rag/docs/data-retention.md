# Data Retention

## Raw Data

Raw training data is kept for 18 months after it is collected. After that, it is deleted from the
data lake and from every backup.

## Personal Data

Personal data, such as names, emails and phone numbers, must be removed from datasets within 30 days
of being collected. Use the `pii-scrub` tool before copying data to a laptop.

## Model Artifacts

Trained models and their evaluation reports are kept for 3 years, so we can explain any past
prediction.
