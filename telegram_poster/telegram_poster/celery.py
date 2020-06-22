import os  
from celery import Celery
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegram_poster.settings')
app = Celery('telegram_poster')  
app.config_from_object('django.conf:settings')  
app.autodiscover_tasks(settings.INSTALLED_APPS) 