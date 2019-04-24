import requests

from bs4 import BeautifulSoup

source = requests.get("https://www.nytimes.com").text

#print(soup.prettify())

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('h2'):

    print(article.text)