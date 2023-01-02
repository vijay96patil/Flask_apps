import json
import requests
from flask import Flask,request

print(dir(Flask))


# data = requests.get("http://127.0.0.1:5000/data")
# print("HTTP GET")
# print(data)
# print()
#
# # For HTTP POST request we need "payload"
# # In this case our "payload" is JSON data
# # Here we are de-serializing Python object (dict) into JSON object (byte-string)
#
# payload = json.dumps({"name":"vijay"})
# data = requests.post("http://127.0.0.1:5000/data",data=payload)
#
# print("HTTP POST")
# print(data)
# print()
