# Use the official Python image as the build image
FROM python:3.14-slim
WORKDIR /app

# Install the dependencies using requirements.txt, in one step, without pip's cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy necessary files
COPY my_script.py .
COPY data/ data/

# Run the script
CMD ["python","my_script.py"]
