from django import forms
from django.conf import settings
from .models import Report

class RequestReport(forms.ModelForm):
    class Meta:
        model = Report

        fields = [
            'name',
            'cryptocurrency'
        ]
        exclude = [
            'slug',
            'image',
            'created_at',
            'updated_at'
        ]
    











    #name = forms.CharField(label='Seu Nome', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rui Lobo'}))
    #cryptocurrency = forms.CharField(label='Cryptomoeda', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: bitcoin'}))