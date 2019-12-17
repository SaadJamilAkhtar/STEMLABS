from django import forms as f
from .models import Complaints, physicianComplaints


class complaintForm(f.ModelForm):
    class Meta:
        model = Complaints
        fields = ['title', 'description']
        labels = {'title': "Title", 'description': "Description"}
        widgets = {
            'title': f.TextInput(attrs={'placeholder': 'TITLE'}),
            'description': f.TextInput(attrs={'placeholder': 'DESCRIPTION'}),
        }


class physicianComplaintForm(f.ModelForm):
    class Meta:
        model = physicianComplaints
        fields = ['title', 'description']
        labels = {'title': "Title", 'description': "Description"}
        widgets = {
            'title': f.TextInput(attrs={'placeholder': 'TITLE'}),
            'description': f.TextInput(attrs={'placeholder': 'DESCRIPTION'}),
        }
