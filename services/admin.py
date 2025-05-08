from django.contrib import admin
from .models import Service, TaskExample, ServiceStage


class TaskExampleInline(admin.TabularInline):
    model = TaskExample
    extra = 1


class ServiceStageInline(admin.TabularInline):
    model = ServiceStage
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [TaskExampleInline, ServiceStageInline]
    prepopulated_fields = {'slug': ('name',)}


