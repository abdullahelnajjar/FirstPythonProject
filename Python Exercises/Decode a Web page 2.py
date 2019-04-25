import requests

from bs4 import BeautifulSoup

source = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").text

#print(soup.prettify())

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('p'):

    print(article.text)