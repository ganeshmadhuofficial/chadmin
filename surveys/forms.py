from django import forms
from surveys import models

class SurveyForm(forms.ModelForm):
  class Meta:
    model  = models.Survey
    fields = ['name','url','is_global','is_special','begin_at','end_at','market','locale']
