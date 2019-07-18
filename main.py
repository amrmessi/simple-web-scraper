import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://yts.pm/browse-movies?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('div', {'class': 'browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4'}):
            href = 'https://yts.pm/' + link.find('a').get('href')
            title = link.find('a', {'class': 'browse-movie-title'}).string
            print(title)
            print(href)
            get_single_item_data(href)
            print('\n')
        page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    print("similar to this =>")
    similar_links = soup.find('div', {'class': 'col-md-6 hidden-xs hidden-sm', 'id': 'movie-related'})
    for link in similar_links.findAll('a'):
        title = link.get('title')
        print(title)


trade_spider(1)
