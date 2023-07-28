import ssl
import certifi
from urllib.request import urlopen


certifi_context = ssl.create_default_context(
	cafile=certifi.where())
print(urlopen('https://sha384.badssl.com/',
	context=certifi_context))
