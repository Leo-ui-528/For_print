from django.db import models
from django.contrib.auth.models import AbstractUser


class PrintUser(AbstractUser):
    position = models.CharField(max_length=64, unique=True, verbose_name='Должность', null=True)
    email = models.EmailField(unique=True, null=True)


