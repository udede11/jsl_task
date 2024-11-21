# Dockerfile.read_file
FROM alpine:3.14

# Install Python3 
RUN apk add --no-cache python3

WORKDIR /app
COPY process_file.py .

CMD ["python3", "process_file.py"]
