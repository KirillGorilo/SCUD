from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    access_code = models.TextField(blank=True)

    def __str__(self):
        return self.name
