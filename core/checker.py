import re
import sys
import requests
from urllib import parse


def is_link(url: str):
    if re.compile(r'https?://(?:www\.)?.+').match(url):
        print('This is a link.')
        return

    print('This is not a link!')
    sys.exit()


def ph_url_check(url: str):
    parsed = parse.urlparse(url)
    regions = ['www', 'cn', 'cz', 'de', 'es', 'fr', 
                    'it', 'nl', 'jp', 'pt', 'pl', 'rt']

    for region in regions:
        if parsed.netloc == region + '.pornhub.com':
            print('Pornhub link found.')
            return
    
    print('Pornhub link not found!')
    sys.exit()


def ph_page_check(url: str):
    response = requests.get(url)
    if response.status_code == 200:
        print('Pornhub page available.')
        return

    print('Pornhub page unavailable!')
    sys.exit()
