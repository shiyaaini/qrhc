import requests
url="https://api.telegram.org/file/bot6469891265:AAFKC2SjxPATJJAR1lswA9dFy34jgsNMrBI/E:\Telegram\1.mp4"
resp=requests.get(url)
print(resp.text)