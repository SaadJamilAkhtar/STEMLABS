from django.contrib import admin
from .models import Complaints, physicianComplaints


@admin.register(Complaints)
class ComplaintPanel(admin.ModelAdmin):
    list_display = ['title', 'date']


@admin.register(physicianComplaints)
class PhysicianComplaintPanel(admin.ModelAdmin):
    list_display = ['title', 'date']
