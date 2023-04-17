import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automation_w_selenium.settings')
app = Celery('automation_w_selenium')

# Configure Celery
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.result_backend = 'db+sqlite:///results.sqlite3'  
CELERY_BROKER_URL = 'redis://localhost:6379/0'

app.autodiscover_tasks()