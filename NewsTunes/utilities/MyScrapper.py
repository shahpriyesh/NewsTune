import requests
import re
import json
from bs4 import BeautifulSoup

NUM_NEWS = 5


class MyScrapper:
    def __init__(self):
        pass

    def get_news(self, category):
        page_link = "https://www.cnn.com/" + category
        page = requests.get(page_link, timeout=5)
        my_pat = re.compile(r'\"articleList\"\:(.*?)]')
        data = re.search(my_pat, str(page.content)).group(1)
        uris = self.get_uris(data)
        newsdata = self.get_news_data(uris)
        return newsdata

    def get_uris(self, data):
        uri_pat = re.compile(r'uri\":\"(.*?)\"')
        uris = re.findall(uri_pat, data)
        return uris

    def get_news_data(self, uris):
        news = []
        i = k = 0
        while i < NUM_NEWS and k < len(uris):
            try:
                headline, newstext = self.scrape_news_from_uri(uris[k])
                news.append([headline, newstext, "https://www.cnn.com" + uris[k]])
                i += 1
            except:
                print("Could not get news for " + uris[k])
            k += 1
        return news

    def scrape_news_from_uri(self, uri):
        page_link = "https://www.cnn.com" + uri
        data = requests.get(page_link, timeout=5)
        soup = BeautifulSoup(data.text, 'html.parser')
        newstext = soup.find('div', {"itemprop": "articleBody"}).get_text()
        headline = soup.title.get_text()
        return headline, newstext

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

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
            info['title'] = title

            # Content
            articleText = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articleText:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            info['data'] = news_paragraph_list

            news.append(info)

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

            # Title
            title = soup.find(class_="pg-headline")
            if title is None:
                title = soup.find(class_="Article__title")
                title = title.get_text()
            else:
                title = title.get_text()
            info['title'] = title

            # Content
            articlebody = soup.find(class_='l-container')
            if articlebody is None:
                articletext = soup.find_all(class_='Paragraph__component')
            else:
                articletext = soup.find_all(class_='zn-body__paragraph')

            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            info['data'] = news_paragraph_list

            news.append(info)

        return news

    def get_usa_news(self):
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

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
                info['title'] = title

            # Content
            articletext = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

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

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
            info['title'] = title

            # Content
            articletext = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

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

            # Title
            title = soup.find(class_="pg-headline")
            if title is not None:
                title = title.get_text()
            info['title'] = title

            # Content
            articletext = soup.find_all(class_='zn-body__paragraph')
            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

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
            info['date'] = date

            # Title
            title = soup.find(class_="PageHead__title")
            if title is not None:
                title = title.get_text()
            info['title'] = title

            # Content
            articletext = soup.find_all(class_='Paragraph__component BasicArticle__paragraph BasicArticle__pad')
            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

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

            # Title
            title = soup.find(class_="Article__title")
            if title is not None:
                title = title.get_text()
            info['title'] = title

            # Content
            articletext = soup.find_all(class_='Paragraph__component')
            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

        return news

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

            # Content
            articletext = soup.find_all('p')
            for paragraph in articletext:
                text = paragraph.get_text()
                news_paragraph_list.append(text)
            if news_paragraph_list:
                info['data'] = news_paragraph_list

            if info:
                news.append(info)

        return news

