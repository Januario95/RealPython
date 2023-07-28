import ssl
from urllib.error import (
	HTTPError, URLError
)
from urllib.request import (
	urlopen, Request
)

def make_request(url):
	try:
		with urlopen(url, timeout=10) as response:
			print(response.status)
			return response.read(), response
	except HTTPError as error:
		print(error.status, error.reason)
	except URLError as error:
		print(error.reason)
	except TimeoutError:
		print('Request timed out')

def make_request2(url, headers=None):
	request = Request(url,
		headers=headers or {})
	try:
		with urlopen(request, timeout=10) as response:
			print(response.status)
			return response.read(), response
	except HTTPError as error:
		print(error.status, error.reason)
	except URLError as error:
		print(error.reason)
	except TimeoutError:
		print('Request timed out')

# make_request('https://httpstat.us/200')
# make_request('https://httpstat.us/403')


# body, response = make_request2(
# 	'https://www.httpbin.org/user-agent',
# 	{'User-Agent': 'Real Python'}
# )
# print(body)
# print(response)

# urlopen('https://superfish.badssl.com/')

unverified_context = ssl._create_unverified_context()
print(urlopen('https://superfish.badssl.com/',
	context=unverified_context))
