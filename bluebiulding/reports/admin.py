from django.contrib import admin
from .models import Report, Cryptocurrency

# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ['cryptocurrency']
    search_fields = ['cryptocurrency']

admin.site.register(Report, ReportAdmin)

class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'slug')


admin.site.register(Cryptocurrency, CryptocurrencyAdmin)