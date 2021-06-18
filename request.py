import requests

url = 'http://localhost:5000/recommend_api'
r = requests.post(url,json={'movie':'Iron Man'})

print(r.json())



