import requests
import re
import json

page_link = "https://www.cnn.com/business"
data = requests.get(page_link, timeout=5)
my_pat = re.compile(r'\"articleList\"\:(.*?)]')
my_json = re.search(my_pat, str(data.content)).group(1)
s = '{"data":'+my_json+']}'
a = json.loads(json.dumps(s))
