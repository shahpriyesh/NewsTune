from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper

def home(request):
    cnn = MyScrapper.MyScrapper()
    news = cnn.get_news('business')
    return render(request, 'home.html', {'news': news})
