from django.contrib import admin

from .models import Store

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'status']
