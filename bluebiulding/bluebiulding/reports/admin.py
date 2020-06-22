from django.contrib import admin
from .models import Report

# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ['cryptocurrency', 'created_at', 'updated_at']
    search_fields = ['cryptocurrency', 'slug']
    prepopulated_fields = {'slug': ('cryptocurrency',)}


admin.site.register(Report, ReportAdmin)