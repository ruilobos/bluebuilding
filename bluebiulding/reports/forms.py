from django.forms import ModelForm
from .models import Report

class RequestReport(ModelForm):
    class Meta:
        model = Report

        fields = '__all__'
    











    #name = forms.CharField(label='Seu Nome', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: Rui Lobo'}))
    #cryptocurrency = forms.CharField(label='Cryptomoeda', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ex: bitcoin'}))