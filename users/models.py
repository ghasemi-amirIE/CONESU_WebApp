from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')
    organization = models.CharField(max_length=150, verbose_name='Organization')
    position = models.CharField(max_length=150, verbose_name='Position')
    avatar = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.organization}" 


