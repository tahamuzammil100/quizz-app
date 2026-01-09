# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app/src/quizapp

# Copy requirements and install
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy the source code
COPY src/ /app/src/

# Set the default command to run the quiz
CMD ["python", "cli.py"]
