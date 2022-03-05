import requests

url = 'http://127.0.0.1:5000/put_books'
myobj = '{"name": "book2", "author": "xyz"}'

x = requests.post(url, data = myobj)

print(x.text)