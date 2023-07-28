import os
import time
import requests
from glob import glob

def get_session():
    return requests.Session()

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = ']' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)


def download_all_sites(sites):
    for url in sites:
        download_site(url)

# if __name__=='__main__':
#     sites = [
#         'https://www.jython.org',
#         'https://www.python.org',
#         # 'http://olympus.realpython.org/dice',
#     ] * 80
#     print('Starting downloads')
#     start = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start
#     print(f'Downloaded {len(sites)} sites in {duration} seconds')


files = glob('*.py')
for file in files:
    new_file = file.replace('-', '_')
    os.rename(file, new_file)