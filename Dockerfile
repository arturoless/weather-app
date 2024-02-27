# Use Python 3.8 slim image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Set environment variable for API key (replace with your actual key)
ENV API_KEY='0eebd1fcf852d29ca0340c5c451d4c9a'
ENV RESERVAMOS_API_URL='https://search.reservamos.mx/api/v2/places'

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
