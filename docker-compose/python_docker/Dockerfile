# Use the official Python base image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script to the container
COPY pyssh.py .

# Install required Python libraries
RUN pip3 install paramiko --break-system-packages

# Define the command to run the script
CMD ["python3", "pyssh.py"]
