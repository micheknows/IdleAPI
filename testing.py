import requests

# data = {
#    "name": "apple",
#    "description": "food",
#    "icon_url": "apple.png"
# }

data = {
   "name": "shekel"
}

response = requests.put("http://127.0.0.1:5000/resources/2", json=data)
print(response.text)