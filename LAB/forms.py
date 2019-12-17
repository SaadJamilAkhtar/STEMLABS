from django import forms as f
from .models import Test, Appointments


class testForm(f.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'description', 'charges', 'average_value']
        labels = {'name': 'TITLE', 'description': "DESCRIPTION", 'charges': "Charges",
                  'average_value': 'AVERAGE VALUE'}



