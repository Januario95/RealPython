import time
import requests
import threading
import concurrent.futures

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, 'session'):
        thread_local.session = requests.Session()

    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        indicator = ']' if 'jython' in url else 'R'
        print(indicator, sep='', end='', flush=True)

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__=='__main__':
    sites = [
        'https://www.jython.org',
        'https://www.python.org',
    ] * 80
    print('Starting downloads')
    start = time.time()
    download_all_sites(sites)
    duration = time.time() - start
    print(f'Downloaded {len(sites)} sites in {duration} seconds')