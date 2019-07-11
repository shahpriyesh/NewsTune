import requests
import re
import json
from bs4 import BeautifulSoup
# page_link = "https://www.cnn.com/business"
# data = requests.get(page_link, timeout=5)
# my_pat = re.compile(r'\"articleList\"\:(.*?)]')
# my_json = re.search(my_pat, str(data.content)).group(1)
# uri_pat = re.compile(r'uri\":\"(.*?)\"')
# uris = re.findall(uri_pat, my_json)
# print(uris[:5])

# uri = "/2019/07/03/business/boeing-100-million-compensation-fund/index.html"
uri = "/2019/07/02/tech/tesla-sales/index.html"
page_link = "https://www.cnn.com"+uri
data = requests.get(page_link, timeout=5)

soup = BeautifulSoup(data.text, 'html.parser')
newstext = soup.find('div',{"itemprop": "articleBody"}).get_text()
print(newstext[:600])

