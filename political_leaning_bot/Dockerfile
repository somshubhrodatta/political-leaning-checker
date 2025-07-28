FROM python:3.10-slim

WORKDIR /app

# Update pip to avoid version issues
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements first to leverage caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Make entrypoint executable
RUN chmod +x entrypoint.sh

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]