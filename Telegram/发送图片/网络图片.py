import requests

# 填入您的机器人的令牌
bot_token = '6469891265:AAFKC2SjxPATJJAR1lswA9dFy34jgsNMrBI'
# 填入您要发送消息的聊天ID（可以是个人用户ID或群组ID）
chat_id = '5846706328'
# 发送消息的URL
url = f'https://api.telegram.org/bot{bot_token}/sendPhoto'
# 要发送的消息内容

# 发送POST请求
data={'chat_id': chat_id,
      'photo':"https://wall.alphacoders.com/big.php?i=1326572",
      }
response = requests.post(url,json=data)
# 检查响应状态码
if response.status_code == 200:
    print('消息已成功发送！')
else:
    print('发送消息时出现问题。')
