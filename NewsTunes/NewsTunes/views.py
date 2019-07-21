from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper
from users.models import News

UPDATE_TIME = 300

def home(request):
    if request.user.is_authenticated:
        cnn = MyScrapper.MyScrapper()
        #News.objects.all().delete()

        if request.user.usa:
            newsList = News.objects.filter(category="USA")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching news from database")
                usanews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="USA").delete()
                print("Fetching USA News")
                usanews = cnn.get_usa_news()
                for news in usanews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author="XYZ",
                        category="USA"
                    )

        if request.user.world:
            print("Fetching World News")
            worldnews = cnn.get_world_news()
            for news in worldnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="World"
                )


        if request.user.business:
            print("Fetching Business News")
            businessnews = cnn.get_business_news()
            for news in businessnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Business"
                )


        if request.user.opinion:
            print("Fetching Opinion News")
            opinionnews = cnn.get_opinion_news()
            for news in opinionnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Opinion"
                )



        if request.user.health:
            print("Fetching Health News")
            healthnews = cnn.get_health_news()
            for news in healthnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Health"
                )

        if request.user.entertainment:
            print("Fetching Entertainment News")
            entertainmentnews = cnn.get_entertainment_news()
            for news in entertainmentnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Entertainment"
                )

        if request.user.style:
            print("Fetching Style News")
            stylenews = cnn.get_style_news()
            for news in stylenews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Style"
                )


        if request.user.travel:
            print("Fetching Travel News")
            travelnews = cnn.get_travel_news()
            for news in travelnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Travel"
                )

        if request.user.sports:
            print("Fetching Sports News")
            sportsnews = cnn.get_sports_news()
            for news in sportsnews:
                News.objects.create(
                    headline=news['title'],
                    body="".join(news['data']),
                    date=news['date'],
                    author="XYZ",
                    category="Sports"
                )

    return render(request, 'home.html', locals())
