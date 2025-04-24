from django.contrib import admin
from .models import (
    CompanyInfo,
)


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin): 
    list_display = ['__str__']