from django.forms import ModelForm
from .models import Report, Cryptocurrency
from django import forms
from django.db import models
from django.forms import ModelChoiceField

class RequestReport(ModelForm):
    class Meta:
        model = Report

        #fields = '__all__'
        fields = ['cryptocurrency']
    
class VisitorReport(forms.Form):
    name = forms.CharField(label='Your Name:', max_length=100)
    cryptocurrency = forms.ModelChoiceField(queryset=Cryptocurrency.objects.all(), to_field_name="symbol") 
