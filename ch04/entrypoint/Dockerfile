# Chapter 3's Dockerfile with ENTRYPOINT + CMD
FROM python:3.14-slim
# Set the working directory inside the container
WORKDIR /app
# Copy and install the requirements first, so code changes don't reinstall them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the project files into the container
COPY . .
# Train the model while the image is built
RUN python train.py
# Document the port the API listens on
EXPOSE 8000

# The fixed part of the command, and its default arguments
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0"]
CMD ["--port", "8000"]
