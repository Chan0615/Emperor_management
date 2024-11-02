from django.db import models
from django.contrib.auth.models import AbstractUser


class Tenant(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)
    is_disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    is_disabled = models.BooleanField(default=False)
