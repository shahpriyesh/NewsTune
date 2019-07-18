from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper

def home(request):
    if request.user.is_authenticated:
        cnn = MyScrapper.MyScrapper()
        if request.user.usa:
            usanews = cnn.get_usa_news()
        if request.user.world:
            worldnews = cnn.get_world_news()
        if request.user.opinion:
            opinionnews = cnn.get_opinion_news()
        if request.user.business:
            businessnews = cnn.get_business_news()
        if request.user.health:
            healthnews = cnn.get_health_news()
        if request.user.entertainment:
            entertainmentnews = cnn.get_entertainment_news()
        if request.user.style:
            stylenews = cnn.get_style_news()
        if request.user.travel:
            travelnews = cnn.get_travel_news()
        if request.user.sports:
            sportsnews = cnn.get_sports_news()
    return render(request, 'home.html', locals())
