import json
import requests


data = requests.get("http://127.0.0.1:5000/data")
print("HTTP GET")
print(data)
print()

data = requests.post(
    "http://127.0.0.1:5000/data",
    data=json.dumps({"name": "prashant"})
)

print("HTTP POST")
print(data)
print()

