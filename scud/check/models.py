from django.db import models
from django.contrib.auth.models import User
import string, random, time

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    access_code = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_group = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    identity_qrcode = models.CharField(max_length=50, blank=True)

    def generate_identity(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))

    def save(self, *args, **kwargs):
        if not self.identity_qrcode:
            self.identity_qrcode = self.generate_identity()
        super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class Security(models.Model):
    pass


