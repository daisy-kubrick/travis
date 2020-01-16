from bs4 import BeautifulSoup
from urllib import request

url = r'https://www.bbc.co.uk/news'
req = request.Request(url)

with reques.urlopen(req) as r:
	soup = r.read()

title = soup.title.string
print(title)