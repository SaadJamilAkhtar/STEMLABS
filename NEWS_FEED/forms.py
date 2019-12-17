from django import forms as f
from .models import NewsFeed


class newsForm(f.ModelForm):
    class Meta:
        model = NewsFeed
        fields = ['title', 'content', 'image']
        labels = {'title': 'TITLE', 'content': "CONTENT", 'image': "IMAGE"}
