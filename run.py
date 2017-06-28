import os
import requests
from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--genre', default='pnf', choices=['hf', 'hnf', 'pnf'])
    args = parser.parse_args()
    options = {
                'hf': 'hardcover-fiction',
                'hnf': 'hardcover-nonfiction',
                'pnf': 'paperback-nonfiction',
              }
    genre = options[args.genre]
    url = 'https://api.nytimes.com/svc/books/v3/lists.json'
    params = {'api-key': os.env['NYTIMES_BOOKS'], 
              'list': genre,
             }
    books = requests.get(url, params=params).json()['results']
    for b in books:
        print('-' * 10)
        link = b['amazon_product_url']
        details = b['book_details'][0] 
        title = details['title']
        description = details['description']
        print(title)
        print(link)
        print(description)
