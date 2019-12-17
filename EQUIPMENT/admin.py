from django.contrib import admin
from .models import Equipment


@admin.register(Equipment)
class EquipmentPanel(admin.ModelAdmin):
    list_display = ['name', 'quantity']
