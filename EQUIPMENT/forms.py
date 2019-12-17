from django import forms as f
from .models import Equipment


class EquipmentEdit(f.Form):
    quantity = f.IntegerField()
