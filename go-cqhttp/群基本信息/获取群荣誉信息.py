import requests,json
resp = requests.get("http://127.0.0.1:5900/get_group_honor_info?group_id=928918816")
print(resp.text)