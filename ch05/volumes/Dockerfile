# Use the official Python image as the base image
FROM python:3.14-slim
# Set the working directory
WORKDIR /app
# Copy the requirements.txt file
COPY requirements.txt ./
# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application files
COPY . .
# Create a directory for storing data
RUN mkdir /app/data

# Define a volume for the data directory
VOLUME /app/data
# Run the application
CMD ["python","main.py"]
