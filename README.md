# Celery Docker Runner

A simple Celery application that demonstrates scheduled tasks running in Docker containers.

## Features
- Celery-based task scheduling
- Tasks executed in separate Docker containers
- Docker-out-of-Docker (DooD) for container isolation and resource management
- Automatic container cleanup
- Configurable task schedule (default: every minute)

## Prerequisites
- Docker
- Docker Compose

## Project Structure
```
.
├── app/
│   ├── celery_app.py     # Celery configuration and initialization
│   └── tasks.py          # Task definitions
├── worker_container/
│   ├── Dockerfile        # Dockerfile for the task container
│   └── process_file.py   # File processing logic
├── files_to_read/        # Directory containing files to be processed
│   └── sample.txt
├── docker-compose.yml    # Main compose file
├── Dockerfile           # Dockerfile for Celery worker
└── requirements.txt     # Python dependencies
```

## Quick Start
1. Clone the repository
2. Place files to be processed in `files_to_read` directory
3. Run:
```bash
docker-compose up --build
```

## How It Works
- Celery Beat scheduler triggers tasks according to defined schedule
- Each task creates a new Docker container using DinD
- Container that runs  `process_file.py` processes files from the `files_to_read` directory
- Container is automatically cleaned up after execution
- Results are logged via Celery worker

## Configuration
Task schedule can be modified in `app/celery_app.py` by updating the `app.conf.beat_schedule` configuration.

## Components
- **Redis**: Message broker for Celery (Can be updated in celery_app.py, SQS is ideal for AWS setup)
- **DooD**: Docker-out-of-Docker service for container isolation and resource management
- **Celery Worker**: Executes the tasks
- **Celery Beat**: Schedules the tasks
- **Worker Container**: Dedicated container for file processing

## License
MIT
