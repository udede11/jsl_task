from celery import Celery
from celery.schedules import crontab

# Initialize Celery app with Redis as broker and backend
app = Celery("tasks", broker="redis://redis:6379/0", backend="redis://redis:6379/0")

# Configure Celery beat schedule
app.conf.beat_schedule = {
    "read-file-every-minute": {
        "task": "tasks.read_file",
        "schedule": crontab(minute="*"),
    },
}
