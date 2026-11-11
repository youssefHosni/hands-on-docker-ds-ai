FROM python:3.14-slim
# The secret is available to this one step, as an environment variable, and is never saved in the image
RUN --mount=type=secret,id=api_key,env=API_KEY \
    python -c "import os; print('Downloading the training data with a key of', len(os.environ['API_KEY']), 'characters')"
