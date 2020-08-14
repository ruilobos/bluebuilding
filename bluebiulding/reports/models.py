from django.db import models

# Create your models here.

class ReportManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(
            models.Q(cryptocurrency__icontains=query) | \
            models.Q(slug__icontains=query)
        )

class Report(models.Model):
    name = models.CharField('Name', max_length=100)
    cryptocurrency = models.CharField('Cryptocurrency', max_length=100)
    slug = models.SlugField('Shortcut')
    image = models.ImageField(upload_to='reports/images', verbose_name='Image', null=True, blank=True)
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Updated at', auto_now=True)
    objects = ReportManager()
    
    def __str__(self):
        return self.cryptocurrency
    
    class Meta:
        verbose_name = "Cryptocurrency"
        verbose_name_plural = "Cryptocurrencies"
        ordering = ['cryptocurrency']