from django import forms as f
from LAB.models import Appointments


class updateProgressForm(f.ModelForm):
    class Meta:
        model = Appointments
        fields = ['progress', 'appointment_date', 'delivery_date', 'result', 'requirements']
