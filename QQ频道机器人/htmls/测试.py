import json,time
with open('config.json','r',encoding='utf-8') as f:
    p=json.loads(f.read())
for i in p['guild']:
    print(i)
dl={"王者":12345}
bn=p['guild'].append(dl)
with open('config.json','w',encoding='utf-8') as f:
    json.dump(p,f,ensure_ascii=False)



for i in p['guild']:
    print(i.keys())