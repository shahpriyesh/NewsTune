import requests
import re
import json
from bs4 import BeautifulSoup


def get_opinion_news():
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

        # Title
        title = soup.find(class_="pg-headline")
        if title is not None:
            title = title.get_text()
            info['title'] = title
        else:
            # if title is not found, skip this news
            continue

        # Content
        articlebody = soup.find(class_='l-container')
        if articlebody is None:
            articlebody = soup.find(class_='Article__body')
            articletext = soup.find_all(class_='Paragraph__component')
        else:
            articletext = soup.find_all(class_=['zn-body__paragraph speakable', 'zn-body__paragraph'])

        for paragraph in articletext:
            text = paragraph.get_text()
            news_paragraph_list.append(text)
        info['data'] = news_paragraph_list

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


news = get_opinion_news()
print_news(news)