from django.contrib import admin
from .models import OrgProfile, Survey

# Register your models here.

admin.site.register(OrgProfile)
admin.site.register(Survey)