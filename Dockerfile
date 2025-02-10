# Use an official lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the web server script
COPY server.py .

# Ensure the static directory exists
RUN mkdir -p /app/static

# Copy the static files into the container
COPY static/ static/

# Expose port 8000
EXPOSE 8000

# Command to run the web server
CMD ["python", "server.py"]

