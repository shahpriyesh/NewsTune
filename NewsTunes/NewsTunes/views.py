from django.http import HttpResponse
from django.shortcuts import render
from utilities import MyScrapper
from users.models import News

UPDATE_TIME = 300

def home(request):
    if request.user.is_authenticated:
        cnn = MyScrapper.MyScrapper()

        #delete news which are older than 5 minutes
        newsList = News.objects.all()
        for item in newsList:
            if item and item.get_time_diff() > UPDATE_TIME:
                News.objects.filter(id=item.id).delete()

        if request.user.usa:
            newsList = News.objects.filter(category="USA")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching USA news from database")
                usanews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="USA").delete()
                print("Fetching USA news from cnn")
                usanews = cnn.get_usa_news()
                for news in usanews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="USA"
                    )

        if request.user.world:
            newsList = News.objects.filter(category="World")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching world news from database")
                worldnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="World").delete()
                print("Fetching world News from cnn")
                worldnews = cnn.get_world_news()
                for news in worldnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="World"
                    )

        if request.user.business:
            newsList = News.objects.filter(category="Business")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching business news from database")
                businessnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Business").delete()
                print("Fetching business News from cnn")
                businessnews = cnn.get_business_news()
                for news in businessnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Business"
                    )


        if request.user.opinion:
            newsList = News.objects.filter(category="Opinion")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching opinion news from database")
                opinionnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Opinion").delete()
                print("Fetching opinion news from cnn")
                opinionnews = cnn.get_opinion_news()
                for news in opinionnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Opinion"
                    )



        if request.user.health:
            newsList = News.objects.filter(category="Health")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching health news from database")
                healthnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Health").delete()
                print("Fetching health news from cnn")
                healthnews = cnn.get_health_news()
                for news in healthnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Health"
                    )

        if request.user.entertainment:
            newsList = News.objects.filter(category="Entertainment")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching entertainment news from database")
                entertainmentnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Entertainment").delete()
                print("Fetching entertainment news from cnn")
                entertainmentnews = cnn.get_entertainment_news()
                for news in entertainmentnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Entertainment"
                    )

        if request.user.style:
            newsList = News.objects.filter(category="Style")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching style news from database")
                stylenews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Style").delete()
                print("Fetching style news from cnn")
                stylenews = cnn.get_style_news()
                for news in stylenews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Style"
                    )


        if request.user.travel:
            newsList = News.objects.filter(category="Travel")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching travel news from database")
                travelnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Travel").delete()
                print("Fetching travel news from cnn")
                travelnews = cnn.get_travel_news()
                for news in travelnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Travel"
                    )

        if request.user.sports:
            newsList = News.objects.filter(category="Sports")
            if newsList and newsList[0].get_time_diff() < UPDATE_TIME:
                print("Fetching sports news from database")
                sportsnews = cnn.convertFromDBToInfo(newsList)
            else:
                News.objects.filter(category="Sports").delete()
                print("Fetching sports news from cnn")
                sportsnews = cnn.get_sports_news()
                for news in sportsnews:
                    wholeNews = ""
                    for para in news['data']:
                        wholeNews = wholeNews + para + "<PB>"
                    entry = News.objects.create(
                        headline=news['title'],
                        body=wholeNews,
                        date=news['date'],
                        author=news['author'],
                        category="Sports"
                    )

    return render(request, 'home.html', locals())
