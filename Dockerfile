# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Create app directory
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port 8000 for the app
EXPOSE 8000

# Start the my app
CMD ["python", "app.py"]
