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
    name = forms.CharField(label='Name:', max_length=100)
    #cryptocurrency = forms.CharField(label='Cryptocurrency:', max_length=100)
    cryptocurrency = forms.ModelChoiceField(queryset=Cryptocurrency.objects.all(), to_field_name="symbol") 
'''

class VisitorReport(ModelForm):
    name = MyFormField(
        label='Name:',
        max_length=200
    )

    class Meta:
        model = Report
        fields = ['name', 'cryptorurrency']
'''







    #name = forms.CharField(label='Seu Nome', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rui Lobo'}))
    #cryptocurrency = forms.CharField(label='Cryptomoeda', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: bitcoin'}))