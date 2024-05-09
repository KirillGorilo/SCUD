from users.models import User
from celery import shared_task


@shared_task
def update_user_ids():
    print('QR-code обновлён')
    users = User.objects.all()
    for user in users:
        user.update_id()
