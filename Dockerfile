# Use Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend /app/backend

# Copy frontend templates and static files
COPY frontend/templates /app/frontend/templates
COPY frontend/static /app/frontend/static

# Copy database folder (keep the same structure)
COPY database /app/database

# Set environment variables for Flask
ENV FLASK_APP=backend/app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
