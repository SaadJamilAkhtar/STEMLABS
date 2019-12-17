from django.db import models as m


class NewsFeed(m.Model):
    title = m.CharField(max_length=300)
    image = m.ImageField(upload_to='images/news', default='images/news/news_default.jpg')
    content = m.TextField()
    date_created = m.DateField(auto_now_add=True, auto_now=False)
    last_updated = m.DateField(auto_now_add=False, auto_now=True)
