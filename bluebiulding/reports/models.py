from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings

# Create your models here.

class ReportManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(
            models.Q(cryptocurrency__icontains=query)
        )

class Report(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cryptocurrency = models.ForeignKey("Cryptocurrency", on_delete=models.SET_NULL, null=True)

    objects = ReportManager()
    
    def __str__(self):
        return self.cryptocurrency
    
    #Return the url to acess a specific instancy of Report
    def get_absolute_url(self):
        return reverse("reports/exhibition.html", args=[str(self.id)])
    
    #String to show the object Report (in ADM site)
    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
        ordering = ['cryptocurrency']


class Cryptocurrency(models.Model):
    slug = models.CharField(max_length=100)
    symbol = models.CharField(max_length=5, 
                            validators=[RegexValidator('^[A-Z_]*$','Only uppercase letters and underscores allowed.')]
                            )

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name = "Cryptocurrecy"
        verbose_name_plural = "Cryptocurrencies"
        ordering = ['symbol']