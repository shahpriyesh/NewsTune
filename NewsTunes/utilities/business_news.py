import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

### Sqlite3 connection open
conn = sqlite3.connect('news_tunes.db')
c = conn.cursor()

### CNN Business news
webpage = requests.get('https://www.cnn.com/business') 
soup = BeautifulSoup(webpage.content, 'html.parser')
urls = soup.find(class_ = 'column zn__column--idx-0').find_all('article')

webpage_urls = []
news_title = []
article_content = []
news_date = []

for link in urls[2:8]:
      url = link.contents[0].find_all('a')[0]   
      webpage_urls.append('https://www.cnn.com'+url.get('href'))

for link in webpage_urls:       
    news_paragraph = []    
    url = link
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    #Date Time
    ndate = soup.find(class_="update-time")
    if ndate != None:
        n_date = ndate.get_text()
        news_date.append(n_date[8:])
    else:
        n_date = None
        news_date.append(n_date)
    
      
    #Title
    ntitle = soup.find(class_="pg-headline")
    if ntitle != None:
        title = ntitle.get_text()
    else:
        title = None
    news_title.append(title)

    #Content
    articlebody = soup.find(class_='l-container')   
    articletext = soup.find_all(class_ = 'zn-body__paragraph speakable')   
    for paragraph in articletext[:-1]:
        text = paragraph.get_text()
        news_paragraph.append(text)
    article_content.append(news_paragraph)   

news_content = [' '.join(article) for article in article_content]

### Business news table
def create_business_table():
    c.execute("CREATE TABLE IF NOT EXISTS business(Title TEXT, PageLink TEXT, Article TEXT, News_Date INTEGER)")


# save articles data to business_news table
def dynamic_news_entry():
    Title = news_title
    PageLink = webpage_urls
    Article = news_content
    News_Date = news_date
    for i in range(len(Title)):
    	c.execute("INSERT INTO business(Title, PageLink, Article, News_Date) VALUES (?, ?, ?, ?)", 
    		(str(Title[i]), str(PageLink[i]), str(Article[i]), str(News_Date[i])))    
    conn.commit()
'''
# Delete 1-day old data from business table
def news_old_deletion():
	c.execute("DELETE FROM business WHERE News_Date <= date('now', '-1 day')")
'''

create_business_table()
dynamic_news_entry()
#news_old_deletion()

### Sqlite3 connection close
c.close
conn.close()


