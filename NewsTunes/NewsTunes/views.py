from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper

def home(request):
    cnn = MyScrapper.MyScrapper()
    # cats = ['business', 'entertainment','politics','sports','world']
    cats = ['business', 'entertainment','politics','world']
    newsdata = {c: cnn.get_news(c) for c in cats}
    print("News obtained from following uris")
#    for c in cats:
#        print(newsdata[c])
    healthnews = cnn.get_health_news()
    worldnews = cnn.get_world_news()
    usanews = cnn.get_usa_news()
    return render(request, 'home.html', locals())
