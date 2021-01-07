import os
from celery import Celery
# from ..thumbnailer.tasks import adding_task
# from thumbnailer.tasks import adding_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'image_parroter.settings')

celery_app = Celery('image_parroter')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()


