import random
import string

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Department(models.Model):
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class User(AbstractUser):
    middle_name = models.CharField(max_length=50, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    course_number = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    identity_qrcode = models.CharField(max_length=50, blank=True)

    def generate_identity(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))

    def update_id(self):
        self.identity_qrcode = self.generate_identity()
        self.save()

    def save(self, *args, **kwargs):
        if not self.identity_qrcode:
            self.identity_qrcode = self.generate_identity()
        super(User, self).save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)