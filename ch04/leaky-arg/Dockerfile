# DON'T DO THIS: a secret passed as a build argument stays in the image's history
FROM python:3.14-slim
ARG API_KEY
RUN echo "Downloading the training data with the API key..."
