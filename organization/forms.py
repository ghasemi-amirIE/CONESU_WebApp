from django import forms
from .models import Organization, Survey

class NewOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class SurveyForm(forms.Form):
        STUDENT = 'STUD'
        EMPLOYEE = 'EMP'
        POSITION_CHOICE = [
            (STUDENT, 'Student'),
            (EMPLOYEE, 'Employee'),]
        widgets = {
            'occupation':forms.Select(choices=POSITION_CHOICE,
            attrs={'class': 'form-control'})
        }

