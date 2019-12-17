from django.contrib import admin
from .models import *


@admin.register(Test)
class TestPanel(admin.ModelAdmin):
    list_display = ['name', 'charges']


@admin.register(Appointments)
class AppointmentPanel(admin.ModelAdmin):
    list_display = ['progress', 'apply_date', 'requirements']
