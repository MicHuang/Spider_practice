from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

url_home = 'https://www.giuem.com/'
folder = 'Giuem'
file_name = 'title'


def create_dir_file(directory, file_name):
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory + '/' + file_name + '.txt', 'w')
    f.close()
    print('file created.')


def append_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


def crawl_title(url, directory, content='title'):

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
        append_file(directory + '/' + content + '.txt', title)
        append_file(directory + '/' + content + '.txt', link + '\n')
    print('Done!')


def crawl_page_title(max_page, directoy, content):
    page = 2
    url = 'https://www.giuem.com/page/' + str(page)
    while page <= max_page:
        crawl_title(url, directoy, content)
        page += 1


create_dir_file(folder, file_name)
crawl_title(url_home, folder, file_name)
crawl_page_title(3, folder, file_name)
