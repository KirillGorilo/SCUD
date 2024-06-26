import random
import string

from django.contrib.auth.models import AbstractUser
from django.db import models


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