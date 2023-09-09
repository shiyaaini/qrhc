import time

import requests,random,string

# cookies = {
#     'PHPSESSID': 'mfq2sv9195lqj3bmft21kt2q6v',
#     'wordpress_test_cookie': 'WP%20Cookie%20check',
# }

for i in range(1000000):
    headers = {
        'authority': 'www.thumbxm.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'PHPSESSID=mfq2sv9195lqj3bmft21kt2q6v; wordpress_test_cookie=WP%20Cookie%20check',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
        'x-requested-with': 'XMLHttpRequest',
    }
    #生成随机数11位

    s = string.ascii_letters
    # 大写string.ascii_uppercase
    # 小写string.ascii_lowercase
    r = random.choice(s)
    d=random.choice(s)
    das=f'{random.randint(111,9999)}{d}{random.randint(3434,898343)}{r}'
    data = {
        'action': 'user_register',
        'user_email': f'{random.randint(1000000,999999999999)}@qq.com',
        'user_pass': das,
        'user_pass2': das,
    }
    print(data)

    response = requests.post('https://www.thumbxm.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    # response.content.decode('unicode_escape')
    print(response.text.encode().decode("unicode_escape"))
    time.sleep(0.2)
