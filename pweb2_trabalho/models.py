from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    cargo = models.CharField(max_length=100, null=True, blank=True)
    setor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
