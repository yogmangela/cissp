# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the Flask app code
COPY . .

# Expose port 5000 for Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]