from django.contrib import admin
from .models import NewsFeed


@admin.register(NewsFeed)
class NewsPanel(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'last_updated']
    list_filter = ['date_created']
    search_fields = ['title']
