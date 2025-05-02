from django.contrib import admin
from .models import (
    Quote, 
    Review, 
    Partner,
    Worker,
    Request,
)


@admin.register(Quote) 
class QuoteAdmin(admin.ModelAdmin): 
    list_display = ['author_name', 'text']


@admin.register(Review) 
class ReviewAdmin(admin.ModelAdmin): 
    list_display = ['author_name', 'name']


@admin.register(Partner) 
class PartnerAdmin(admin.ModelAdmin): 
    list_display = ['name']


@admin.register(Worker) 
class WorkerAdmin(admin.ModelAdmin): 
    list_display = ['name', 'position']


@admin.register(Request) 
class RequestAdmin(admin.ModelAdmin): 
    list_display = ['name', 'phone']
