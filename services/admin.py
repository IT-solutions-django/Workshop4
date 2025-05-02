from django.contrib import admin
from .models import Service, TaskExample


class TaskExampleInline(admin.TabularInline):
    model = TaskExample
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [TaskExampleInline]



