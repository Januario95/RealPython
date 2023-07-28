import json
from pprint import pprint
from urllib.request import urlopen

# with urlopen("https://realpython.com/urllib-request/") as response:
# 	body = response.read()


# print(body[:15])

url = 'https://jsonplaceholder.typicode.com/todos/1'
# with urlopen(url) as response:
# 	body = response.read()

# todo_item = json.loads(body)
# print(todo_item)


# with urlopen(url) as response:
# 	pprint(dir(response))


example = 'https://www.example.com'
# with urlopen(url) as response:
# 	pass

# pprint(response.headers)
# print(response.headers)
# # pprint(response.headers.items())
# print(response.getheader('Server'))
# print(response.headers['Server'])

# response = urlopen(url)
# body = response.read()
# response.close()
# print(response.closed)
# print(json.loads(body))

# try:
# 	response = urlopen(url)
# except Exception as e:
# 	print(e)
# else:
# 	body = response.read()
# finally:
# 	if response is not None:
# 		response.close()

# print(json.dumps(
# 	json.loads(body),
# 	indent=4))

# with urlopen('http://localhost:8000/api/products/') as response:
# 	# data = response.read()
# 	print(response.read(50))
# 	print(response.read(50))

# # print(data)
# print(response.read(50))


# Another point to note is that you 
# can’t reread a response once you’ve 
# read all the way to the end:

# my_url = 'http://localhost:8000/api/products/'
# with urlopen(my_url) as response:
# 	first_read = response.read()
# 	second_read = response.read()

# print(len(first_read))
# print(len(second_read))


# with urlopen(url) as response:
# 	body = response.read()

# # decoded_body = body.decode('utf-8')
# # print(decoded_body[:30])

# character_set = response.headers.get_content_charset()
# print(character_set)

test = 'http://localhost:8000/user/index/test/'
# with urlopen(test) as response:
# 	body = response.read()

# character_set = response.headers.get_content_charset()
# print(character_set)
# decoded_body = body.decode(character_set)
# print(decoded_body[:30])


# with urlopen(test) as response:
# 	body = response.read()

# with open('example.html', mode='wb') as html:
# 	html.write(body)


# with urlopen('https://pdfmyurl.com/') as response:
# 	body = response.read()

# with open('pdfmyurl.html', mode='wb') as html:
# 	html.write(body)


# with urlopen('https://www.google.com') as response:
# 	body = response.read()

# character_set = response.headers.get_content_charset()
# print(character_set)

# content = body.decode(character_set)
# with open('google.html', encoding='utf-8', mode='w') as file:
# 	file.write(content)


with urlopen('https://httpbin.org/json') as response:
	body = response.read()

character_set = response.headers.get_content_charset()
print(character_set)

