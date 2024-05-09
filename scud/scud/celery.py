from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scud.settings')

app = Celery('scud')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'update_user_ids_every_5_seconds': {
        'task': 'check.tasks.update_user_ids',
        'schedule': 180.0,
    },
}

app.conf.timezone = 'UTC'
