import requests
import re
import json
from bs4 import BeautifulSoup


def get_sports_news():
    # CNN Sports news
    page = requests.get('https://bleacherreport.com/')
    soup = BeautifulSoup(page.content, 'html.parser')
    layout = soup.find(class_='organism contentStream featuredArticles')
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

        # Title
        title = soup.find('h1')
        if title is not None:
            title = title.get_text()
            info['title'] = title
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


news = get_sports_news()
print_news(news)