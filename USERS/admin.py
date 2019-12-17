from django.contrib import admin
from .models import Admin, Patient, user, Physician


@admin.register(Admin)
class AdminPanel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cnic']


@admin.register(Patient)
class PatientPanel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cnic', 'image', 'id']


@admin.register(Physician)
class PhysicianPanel(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'cnic', 'image', 'id']


@admin.register(user)
class UserPanel(admin.ModelAdmin):
    list_display = ['username', 'password']
