import requests
import re
import json
from bs4 import BeautifulSoup
import datetime

NUM_NEWS = 5


class MyScrapper:
    def __init__(self):
        pass

    def print_news(self, news):
        for n in news:
            print("Date = ", n['date'])
            print("Title = ", n['title'])
            for idx in range(len(n['data'])):
                print("Para-", idx, ") ", n['data'][idx])
            print()
            print()

    def get_usa_news(self):
        # CNN USA news
        webpage = requests.get('https://www.cnn.com/us')
        soup = BeautifulSoup(webpage.content, 'html.parser')
        urls = soup.find(class_='column zn__column--idx-0').find_all('article')

        webpage_urls = []
        news = []

        for link in urls[:8]:
            url = link.contents[0].find_all('a')[0]
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            info['date'] = date

            # Author
            author = soup.find(class_="metadata__byline__author")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articletext = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

            if len(news) >= 5:
                break

        return news

    def get_world_news(self):
        # CNN World news
        webpage = requests.get('https://www.cnn.com/world')
        soup = BeautifulSoup(webpage.content, 'html.parser')
        urls = soup.find(class_='column zn').find_all('article')

        webpage_urls = []
        news = []

        for link in urls[:8]:
            url = link.contents[0].find_all('a')[0]
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            info['date'] = date

            # Author
            author = soup.find(class_="metadata__byline__author")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            else:
                # if title is not found, skip this news
                continue
            info['author'] = author

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articlebody = soup.find(class_='l-container')
            if articlebody is None:
                articletext = soup.find_all(class_='Paragraph__component')
            else:
                articletext = soup.find_all(class_='zn-body__paragraph')

            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            info['data'] = news_paragraph_list

            if info:
                news.append(info)
                
            if len(news) >= 5:
                break

        return news

    def get_business_news(self):
        # CNN Business news
        page = requests.get('https://www.cnn.com/business')
        soup = BeautifulSoup(page.content, 'html.parser')
        urls = soup.find(class_='column zn__column--idx-0').find_all('article')

        webpage_urls = []
        news = []

        for link in urls[2:8]:
            url = link.contents[0].find_all('a')[0]
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            info['date'] = date

            # Author
            author = soup.find(class_="metadata__byline__author")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articletext = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

            if len(news) >= 5:
                break

        return news

    def get_opinion_news(self):
        # CNN World news
        webpage = requests.get('https://www.cnn.com/opinions')
        soup = BeautifulSoup(webpage.content, 'html.parser')
        urls = soup.find(class_='column zn').find_all('article')

        webpage_urls = []
        news = []

        for link in urls[:8]:
            url = link.contents[0].find_all('a')[0]
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            info['date'] = date

            # Author
            author = soup.find(class_="metadata__byline__author")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articlebody = soup.find(class_='pg-rail-tall__body')
            if articlebody is None:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            else:
                articletext = articlebody.find_all(class_='zn-body__paragraph')

            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            info['data'] = news_paragraph_list

            news.append(info)

            if len(news) >= 5:
                break
        return news

    def get_health_news(self):
        # CNN Health news
        page = requests.get('https://www.cnn.com/health')
        soup = BeautifulSoup(page.content, 'html.parser')
        urls = soup.find(class_='column zn__column--idx-0').find_all('article')

        webpage_urls = []
        news = []

        for link in urls[:4]:
            url = link.contents[0].find_all('a')[0]
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            page = requests.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            info['date'] = date

            # Author
            author = soup.find(class_="metadata__byline__author")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articleText = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articleText:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            info['data'] = news_paragraph_list

            news.append(info)

            if len(news) >= 5:
                break

        return news

    def get_entertainment_news(self):
        # CNN Entertainment news
        page = requests.get('https://www.cnn.com/entertainment')
        soup = BeautifulSoup(page.content, 'html.parser')
        urls = soup.find(class_ = 'column zn__column--idx-2').find_all('article')

        webpage_urls = []
        news = []

        for link in urls[:8]:
            url = link.contents[0].find_all('a')[0]
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            info['date'] = date

            # Author
            author = soup.find(class_="metadata__byline__author")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articletext = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

            if len(news) >= 5:
                break

        return news

    def get_style_news(self):
        # CNN Entertainment news
        page = requests.get('https://www.cnn.com/style')
        soup = BeautifulSoup(page.content, 'html.parser')
        layout = soup.find(class_='LayoutGrid__component')
        urls = layout.findAll(class_='CardBasic__thumb')

        webpage_urls = []
        news = []

        for link in urls[:8]:
            url = link.find('a')
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # Date Time
            date = soup.find(class_="update-time")
            if date is not None:
                date = date.get_text()
                date = date[8:]
            else:
                date = datetime.datetime.now()
                date = date.strftime("%I:%M %p PT, %a %B %d, %Y")
                #1:30 PM ET, Sat July 20, 2019
            info['date'] = date

            # Author
            author = soup.find(class_="Authors__writer")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="PageHead__title")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articletext = soup.find_all(class_='Paragraph__component BasicArticle__paragraph BasicArticle__pad')
            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

            if len(news) >= 5:
                break

        return news

    def get_travel_news(self):
        # CNN Travel news
        page = requests.get('https://www.cnn.com/travel')
        soup = BeautifulSoup(page.content, 'html.parser')
        layout = soup.find(class_='Homepage__primary')
        urls = layout.findAll(class_='CardBasic__thumb')

        webpage_urls = []
        news = []

        for link in urls:
            url = link.find('a')
            webpage_urls.append('https://www.cnn.com' + url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # Date Time
            date = soup.find(class_="Article__subtitle")
            if date is not None:
                date = date.get_text()
            info['date'] = date

            # Author
            author = soup.find(class_="Article__subtitle")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find(class_="Article__title")
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articletext = soup.find_all(class_='Paragraph__component')
            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

            if len(news) >= 5:
                break

        return news

    def get_sports_news(self):
        # CNN Sports news
        page = requests.get('https://bleacherreport.com/')
        soup = BeautifulSoup(page.content, 'html.parser')
        layout = soup.find(class_='organism contentStream featuredArticles')
        #print(layout)
        urls = layout.findAll(class_='articleContent')

        webpage_urls = []
        news = []

        for link in urls:
            url = link.find('a')
            webpage_urls.append(url.get('href'))

        for link in webpage_urls:
            info = {}
            news_paragraph_list = []
            url = link
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.text, 'html.parser')

            # Date Time
            date = soup.find(class_="date")
            if date is not None:
                date = date.get_text()
            info['date'] = date

             # Author
            author = soup.find(class_="name")
            if author is not None:
                author = author.get_text()
                author = author[:]
                #print(author)
            info['author'] = author

            # Title
            title = soup.find('h1')
            if title is not None:
                title = title.get_text()
                info['title'] = title
                print("Fetching -> ", title)
            else:
                # if title is not found, skip this news
                continue

            # Content
            articletext = soup.find_all('p')
            for paragraph in articletext:
                text = paragraph.get_text().strip()
                if text != "":
                    news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

        return news

    def convertFromDBToInfo(self, newsset):
        news = []
        for item in newsset:
            info = {}
            news_paragraph_list = []

            info['date'] = item.date
            info['title'] = item.headline
            info['author'] = item.author
            news_paragraph_list = item.body.split("<PB>")
            info['data'] = news_paragraph_list

            if info:
                news.append(info)

            if len(news) >= 5:
                break
        return news

