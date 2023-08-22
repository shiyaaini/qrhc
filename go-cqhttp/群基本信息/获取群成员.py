import requests,json
resp = requests.get("http://127.0.0.1:5900/get_group_member_info?group_id=928918816&user_id=2106359814")
print(resp.text)