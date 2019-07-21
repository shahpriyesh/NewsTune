import requests
import re
import json
from bs4 import BeautifulSoup


def get_usa_news():
    # CNN Business news
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
        author_list = []
        '''author = soup.find(class_= "metadata__byline__author")
        if author is not None:
            author_list = author.findAll(a)
            print(author_list)'''

        # Author
        author = soup.find(class_="metadata__byline__author")
        if author is not None:
            author = author.get_text()
            author = author[:]
            print(author)
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


def print_news(news):
    for n in news:
        print("Date = ", n['date'])
        print("Title = ", n['title'])
        for idx in range(len(n['data'])):
            print("Para-", idx, ") ", n['data'][idx])
        print()
        print()


news = get_usa_news()
print_news(news)