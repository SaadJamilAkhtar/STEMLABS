from django.db import models as m
from datetime import date
from USERS.models import Patient


class Test(m.Model):
    name = m.CharField(max_length=50, null=False, blank=False)
    description = m.CharField(max_length=500, null=False)
    charges = m.IntegerField(null=False, blank=False)
    average_value = m.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Appointments(m.Model):
    progress_state = [("Pending", "Pending"), ("In Progress", "In Progress"),
                      ("Waiting for receiver", "Waiting for receiver"), ("Delivered", "Delivered")]
    apply_date = m.DateField(auto_now_add=True)
    patient_id = m.ForeignKey(Patient, on_delete=m.CASCADE)
    appointment_date = m.DateField(default='2000-01-01')
    requirements = m.BooleanField(default=False)
    progress = m.CharField(max_length=50, choices=progress_state, default='Pending')
    delivery_date = m.DateField(default='2000-01-01')
    test_id = m.ForeignKey(Test, on_delete=m.CASCADE)
    result = m.FileField(upload_to='files/results')

    class Meta:
        verbose_name_plural = "Appointments"
