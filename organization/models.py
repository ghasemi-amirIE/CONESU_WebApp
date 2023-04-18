from django.db import models

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser
import datetime

# Create your models here.
class OrgProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200, blank=False)
    logo = models.ImageField(blank=True, upload_to='uploads')
    vision = models.CharField(max_length=250, blank=True)
    mission = models.CharField(max_length=500, blank=True)
    num_employees = models.CharField(max_length=20)
    founded = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(datetime.datetime.now().year)])
    email = models.EmailField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.title}"

class Survey(models.Model):
    STUDENT = 'STUD'
    EMPLOYEE = 'EMP'
    POSITION_CHOICE = [
            (STUDENT, 'Student'),
            (EMPLOYEE, 'Employee'),]
    organization = models.OneToOneField(OrgProfile, on_delete= models.CASCADE)
    satsified = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(10)])
    period = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(40)])
    occupation = models.CharField(max_length=10, choices=POSITION_CHOICE)
    participant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
   
