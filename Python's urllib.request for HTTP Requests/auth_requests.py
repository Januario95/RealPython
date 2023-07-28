import ssl
from urllib.error import (
	HTTPError, URLError
)
from urllib.request import (
	urlopen, Request
)


def make_request(url, headers=None):
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

token = 'abcdefghijklmnopqrstuvwxyz'
headers = {
	'Authorization': f'Bearer {token}'
}
print(make_request(
	'https://httpbin.org/bearer',
	headers))
