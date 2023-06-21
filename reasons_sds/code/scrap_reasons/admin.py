from django.contrib import admin
from . import models
import datetime
import time


@admin.register(models.Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    readonly_fields = ['id']


@admin.register(models.Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'operation', 'type']
    list_filter = ['type','operation']
    ordering = ['id']
    readonly_fields = ['id']
