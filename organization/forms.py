from django import forms
from .models import Survey, OrgProfile

class NewOrgForm(forms.ModelForm):
    class Meta:
        model = OrgProfile
        fields = '__all__'

class SurveyForm(forms.ModelForm):
       class Meta:
            model = Survey
            fields = ['organization','satsified','period','occupation',]