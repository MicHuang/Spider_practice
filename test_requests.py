import requests
from bs4 import BeautifulSoup

url = "https://www.github.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

for link in soup.find_all('a'):
    print(url + link.get('href'))
