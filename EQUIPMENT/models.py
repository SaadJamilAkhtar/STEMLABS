from django.db import models as m


class Equipment(m.Model):
    name = m.CharField(max_length=30, null=False, blank=False)
    description = m.TextField(default='None')
    quantity = m.IntegerField(default=0)
    last_stocked = m.DateField(auto_now_add=False, auto_now=True)
