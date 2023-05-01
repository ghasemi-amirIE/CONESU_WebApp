from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import CustomUser
import datetime

#Model for organizations
class OrgProfile(models.Model):
    title = models.CharField(max_length=200, blank=False)
    logo = models.ImageField(upload_to='org_logo')
    vision = models.CharField(max_length=250, blank=True)
    mission = models.CharField(max_length=500, blank=True)
    num_employees = models.CharField(max_length=20)
    founded = models.PositiveIntegerField(validators=[MinValueValidator(1000), MaxValueValidator(datetime.datetime.now().year)])
    email = models.EmailField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.title}"

#Basic survey model. It now stores both questions and answers, this is a simple solution that needs to be rebuild.
class Survey(models.Model):
    STUDENT = 'STUD'
    EMPLOYEE = 'EMP'
    POSITION_CHOICE = [
            (STUDENT, 'Student'),
            (EMPLOYEE, 'Employee'),]
    
    organization = models.ForeignKey(OrgProfile, on_delete= models.CASCADE)
    satsified = models.IntegerField( validators=[MinValueValidator(1), MaxValueValidator(10)])
    period = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(40)])
    occupation = models.CharField(max_length=10, choices=POSITION_CHOICE)
    participant = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Surveys'

    
#Model for contact form on landing page. Might create an abstract user model to store often used fields
class Contact(models.Model):
    name = models.CharField(max_length=100, name="Full name")
    organization = models.CharField(max_length=100, name = "Company")
    role = models.CharField(max_length=100, name ="Role")
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=20, blank = True)

    def __str__(self):
        return f"{self.name} {self.organization}-{self.role}"

   
