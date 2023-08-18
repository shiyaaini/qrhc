import requests,json
authorization='hmp_13cf3b02279ef7585f8981074f130e5d372004728fd2296b93a2181f22d39fab'
class Hamibot:
  def __init__(self,authorization,urls):
    self.authorization=authorization
    self.urls=urls
  #获取机器人列表
  def bot_list(self):
    url=f"{self.urls}/v1/robots"
    headers={
      "authorization":self.authorization,

    }
    resp=requests.get(url=url,headers=headers)
    p=json.loads(resp.text)
    #判断是否有机器人
    if p['count']==0:
      return {"msg":"没有机器人"}
    else:
      ps={}
      for i in p['items']:
        id=i['_id']
        brand=i['brand']
        model=i['model']
        appVersion=i['appVersion']
        name=i['name']
        ps[name]={'id':id,'brand':brand,'model':model,'appVersion':appVersion}
      print(ps)
      return ps

  #获取脚本id
  def script_id(self):
    url=f"{self.urls}/v1/scripts"
    headers={'authorization':self.authorization}
    resp=requests.get(url=url,headers=headers)
    p=json.loads(resp.text)
    ps={}
    #判断是否有脚本
    if p['count']==0:
      return {"msg":"没有脚本"}
    else:
      for i in p['items']:
        id=i['_id']
        name=i['name']
        ps[name]=id
      print(ps)
      return ps
  #获取开发者脚本
  def script_dev(self):
    url=f"{self.urls}/v1/devscripts"
    headers={'authorization':self.authorization}
    resp=requests.get(url=url,headers=headers)
    p=json.loads(resp.text)
    ps={}
    #判断是否有脚本
    if p['count']==0:
      return {"msg":"没有脚本"}
    else:
      for i in p['items']:
        id=i['_id']
        name=i['name']
        ps[name]=id
      print(ps)
      return ps

  #运行指定脚本
  def run_script(self):
    script_id='644882a05531916b9bab560b'
    url=f"{self.urls}/v1/devscripts/{script_id}/run"
    headers={'authorization':self.authorization}
    data={"robots":[{"_id":"64c3962f1f5f0cedf1e95c9a","name":"灵透茄子"}]}
    resp=requests.post(url=url,headers=headers,json=data)
    print(resp.text)



if __name__=="__main__":
  urls="https://api.hamibot.com"
  bot=Hamibot(authorization,urls)
  # bot.bot_list()
  # bot.script_id()
  # bot.script_dev()
  bot.run_script()