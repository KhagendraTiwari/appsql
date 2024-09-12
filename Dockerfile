# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variables (optional, can be overridden by docker-compose.yml)
ENV DB_HOST=db
ENV DB_USER=root
ENV DB_PASSWORD=rootpassword
ENV DB_NAME=mydb

# Run app.py when the container launches
CMD ["python", "app.py"]
