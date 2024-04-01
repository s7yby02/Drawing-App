# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Flask app code to the container
COPY web /app

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
