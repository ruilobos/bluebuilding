from django.db import models

# Create your models here.

class ReportManager(models.Manager):

    def search(self,query):
        return self.get_queryset().filter(
            models.Q(cryptocurrency__icontains=query) | \
            models.Q(slug__icontains=query)
        )

class Report(models.Model):
    name = models.CharField('Nome', max_length=100)
    cryptocurrency = models.CharField('Cryptomoeda', max_length=100)
    slug = models.SlugField('Atalho')
    image = models.ImageField(upload_to='reports/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    objects = ReportManager()
    
    def __str__(self):
        return self.cryptocurrency
    
    class Meta:
        verbose_name = "Cryptomoeda"
        verbose_name_plural = "Cryptomoedas"
        ordering = ['cryptocurrency']