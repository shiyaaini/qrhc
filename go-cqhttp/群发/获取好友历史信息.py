import requests,time

# 配置参数
bot_server = "http://127.0.0.1:5900"  # go-cqhttp 服务地址
friend_id = 2106359814  # 好友的 QQ 号
start_time = int(time.time())-1000  # 开始时间戳，表示从 2021-06-10 00:00:00 开始获取消息
end_time = int(time.time())  # 结束时间戳，表示到 2021-06-11 00:00:00 为止获取消息

# 获取历史消息
response = requests.get(bot_server + "/get_msg", params={
    "user_id": friend_id,
    "message_history": True,
    "start_time": start_time,
    "end_time": end_time
})
print(response.text)
messages = response.json()["data"]

# 处理历史消息
for message in messages:
    text = message["message"]
    print(text)
