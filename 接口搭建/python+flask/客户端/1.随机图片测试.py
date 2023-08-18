import requests
url="http://127.0.0.1:5000/index"
data={
    "name":"shiya",
    "age":10,
    "city":"广东"
}
resp=requests.post(url,data=data)
print(resp.text)