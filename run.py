import random
import re
import requests
from bs4 import BeautifulSoup


class GoogleResultException(Exception):
    pass


def is_book(tag):
    return len(tag.contents) >= 1 and tag.contents[0].name == 'strong'


def main(url):
    r = requests.get(url)
    if r.status_code >= 400:
        raise requests.HTTPError
    soup = BeautifulSoup(r.content, 'html.parser')
    site = soup.find(href=re.compile('nytimes')).get('href', '')
    pattern = re.compile(r'.*(https?://.+)&.*')
    match = pattern.match(site)
    href = match.groups(1)[0] if match else None
    if not href:
        raise GoogleResultException
    r = requests.get(href)
    if r.status_code >= 400:
        raise requests.HTTPError
    soup = BeautifulSoup(r.content, 'html.parser')
    books = [l.text for l in soup.find_all(is_book)]
    return (books, r.url)


if __name__ == '__main__':
    url = 'https://www.google.com/search?q=books+we+recommend+this+week'
    books, url = main(url)
    print url
    print random.choice(books)
