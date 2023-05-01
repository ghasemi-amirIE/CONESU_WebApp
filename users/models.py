from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

#Custom User model has additional fields. Using UUID to prevent guessing urls 
class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=150, verbose_name='First name')
    last_name = models.CharField(max_length=150, verbose_name='Last name')
    organization = models.ForeignKey('organization.OrgProfile', blank=True, null=True, on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=150, verbose_name='Position')
    avatar = models.ImageField(upload_to="avatars")

    class Meta:
        order_with_respect_to = 'organization'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.organization}"
