import time
import requests
import multiprocessing

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        indicator = multiprocessing.current_process().name[-1]
        print(indicator, sep='', end='', flush=True)

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)
    
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