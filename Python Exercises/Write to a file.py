import requests

from bs4 import BeautifulSoup

source = requests.get("https://www.nytimes.com").text

#print(soup.prettify())

soup = BeautifulSoup(source, 'lxml')

file_name = input('Please enter the file name to be saved in: ')

with open(file_name+'.txt', 'w') as open_file:
    for article in soup.find_all('h2'):
        open_file.write(article.text + '\n')

