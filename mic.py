from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url_home = 'https://www.giuem.com/'


def crawl_title(url):

    print('Opening the webpage...')
    response = urlopen(url)
    souce_code = response.read()

    if response.getcode() is not 200:
        print("Can't reach the website....")
        return

    print('Webpage is opened...')
    soup = BeautifulSoup(souce_code, 'html.parser')
    nodes = soup.select('h2.post-title a[href]')
    print('Targeting the title...')
    for node in nodes:
        title = node.string
        link = url + str(node['href'])
        print(title)
        print(link)
        print()


def crawl_page_title(max_page):
    page = 2
    url = 'https://www.giuem.com/page/' + str(page)
    while page <= max_page:
        crawl_title(url)
        page += 1


crawl_title(url_home)
crawl_page_title(4)
