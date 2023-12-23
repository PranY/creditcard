# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the required files and directory into the container at /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# Copy files from S3 inside docker
RUN mkdir /app/models
RUN aws s3 cp s3://creditcard-project/models/model.joblib /app/models/model.joblib

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
