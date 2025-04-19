# Dockerfile

FROM python:3.10-slim

# Set a working directory
WORKDIR /app

# Copy dependency lists and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your app code
COPY . .

# Expose the port Flask will run on
EXPOSE 5000

# Tell Flask where to find your app
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Default command to start the server
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
