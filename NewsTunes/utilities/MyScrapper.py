import requests
import re
import json

class MyScrapper:
    def __init__(self):
        pass

    def get_news(self, category):
        page_link = "https://www.cnn.com/"+category
        data = requests.get(page_link, timeout=5)
        my_pat = re.compile(r'\"articleList\"\:(.*?)]')
        my_json = re.search(my_pat, str(data.content)).group(1)
        s = '{"data":'+my_json+']}'
        return s
