import requests

# 填入您的机器人的令牌
bot_token = '6469891265:AAFKC2SjxPATJJAR1lswA9dFy34jgsNMrBI'
# 发送消息的URL
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
# 发送POST请求
data={'chat_id': 5846706328, 'text': "#你好\nlove you"}
response = requests.post(url, json=data)
# 检查响应状态码
if response.status_code == 200:
    print('消息已成功发送！')
else:
    print('发送消息时出现问题。')
