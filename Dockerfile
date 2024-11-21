FROM python:3.9

# Install Docker
RUN apt-get update && \
    apt-get install -y docker.io

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "tasks", "worker", "--loglevel=info"]
