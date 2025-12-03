import requests

#get - get data from server
#post - post data in server


res=requests.get("")#API URL with KEY
print(res.json())
