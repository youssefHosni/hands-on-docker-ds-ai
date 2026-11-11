# The same Dockerfile as Chapter 3, on Alpine
FROM python:3.14-alpine
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
# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
