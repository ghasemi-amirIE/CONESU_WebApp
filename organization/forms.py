from django import forms
from .models import Organization, Survey

class NewOrgForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class SurveyForm(forms.ModelForm):
       class Meta:
            model = Survey
            fields = ['organization','satsified','period','occupation',]

