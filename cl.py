from bs4 import BeautifulSoup
import requests


def just_crawl(max_page):
    page = 1
    url = 'http://www.t66y.com/thread0806.php?fid=16&search=&page=' + str(page)

    while page <= max_page:
        souce_code = requests.get(url)
        plain_text = souce_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        links = soup.findAll('font')
        f = open('cl.txt', 'w')
        for link in links:
            title = link.string
            f.write(title + '\n')
        page += 1
        f.close()


just_crawl(1)
