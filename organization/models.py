from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Organization(models.Model):
    title = models.CharField(max_length=200, blank=False)
    logo = models.ImageField(blank =True, upload_to = 'uploads')
    vision = models.CharField(max_length=250, blank=True)
    mission = models.CharField(max_length=500, blank=True)
    num_employees = models.CharField(max_length=20)
    founded = models.CharField(max_length=4)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.title}"

class Survey(models.Model):
    STUDENT = 'STUD'
    EMPLOYEE = 'EMP'
    POSITION_CHOICE = [
            (STUDENT, 'Student'),
            (EMPLOYEE, 'Employee'),]

    organization = models.ForeignKey(Organization, on_delete= models.CASCADE)
    satsified = models.IntegerField(max_length=2, 
                                    validators=[MinValueValidator(1), MaxValueValidator(10)])
    period = models.IntegerField(max_length=2,
                                 validators=[MinValueValidator(1), MaxValueValidator(40)])
    occupation = models.CharField(max_length=10, choices=POSITION_CHOICE)
    
   
