from django.shortcuts import render
from .models import NewsFeed


def showNews(request):
    news = NewsFeed.objects.all()
    news = news.reverse()
    if news:
        latest = news[:3]
        para = {'news': news, 'latest': latest}
        return render(request, 'USERS/news.html', para)
    else:
        message = 'No news added yet'
        para = {'message': message}
        return render(request, 'USERS/news.html', para)
