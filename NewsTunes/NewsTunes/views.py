from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper

def home(request):
    cnn = MyScrapper.MyScrapper()
    usanews = cnn.get_usa_news()
    worldnews = cnn.get_world_news()
    #politicsnews = cnn.get_politics_news()
    businessnews = cnn.get_business_news()
    healthnews = cnn.get_health_news()
    entertainmentnews = cnn.get_entertainment_news()
    stylenews = cnn.get_style_news()
    travelnews = cnn.get_travel_news()
    sportsnews = cnn.get_sports_news()
    return render(request, 'home.html', locals())
