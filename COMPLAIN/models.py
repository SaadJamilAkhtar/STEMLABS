from django.db import models as m
from USERS.models import Patient, Physician


class Complaints(m.Model):
    title = m.CharField(max_length=200)
    description = m.TextField()
    patient_id = m.ForeignKey(Patient, on_delete=m.CASCADE)
    date = m.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = "Complaints"


class physicianComplaints(m.Model):
    title = m.CharField(max_length=200)
    description = m.TextField()
    physician_id = m.ForeignKey(Physician, on_delete=m.CASCADE)
    date = m.DateField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = "Physician Complaints"
