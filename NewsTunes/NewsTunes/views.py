from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper
from users.models import News

def home(request):
    if request.user.is_authenticated:
        cnn = MyScrapper.MyScrapper()
        if request.user.usa:
            print("Fetching USA News")
            usanews = cnn.get_usa_news()
            for news in usanews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="USA"
                )
        if request.user.world:
            print("Fetching Wolrd News")
            worldnews = cnn.get_world_news()
        if request.user.opinion:
            print("Fetching Opinion News")
            opinionnews = cnn.get_opinion_news()
        if request.user.business:
            print("Fetching Business News")
            businessnews = cnn.get_business_news()
        if request.user.health:
            print("Fetching Health News")
            healthnews = cnn.get_health_news()
        if request.user.entertainment:
            print("Fetching Entertainment News")
            entertainmentnews = cnn.get_entertainment_news()
        if request.user.style:
            print("Fetching Style News")
            stylenews = cnn.get_style_news()
        if request.user.travel:
            print("Fetching Travel News")
            travelnews = cnn.get_travel_news()
        if request.user.sports:
            print("Fetching Sports News")
            sportsnews = cnn.get_sports_news()
    return render(request, 'home.html', locals())
