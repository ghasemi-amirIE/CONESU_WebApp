from django.contrib import admin
from .models import Organization, Survey

# Register your models here.

admin.site.register(Organization)
admin.site.register(Survey)