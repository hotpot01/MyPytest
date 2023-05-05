import json
import requests
import threading
from faker import Faker


#获取token,业务接口，都可以进行封装
#不仅是造数据，也可以用来做测试

#获取token
#online的自建应用
# appid="cli_a3ee06d2463cd00d"
# appsecret="o9HuYTAAT8ugwYLBUZ33cceqWZpfCRHJ"
#boe公用的自建应用
# appid="cli_a3d5d192aff8d01b"
# appsecret="LexA85Jf2CypkhKWzBEqCcnbGfobjdSk"
#staging的自建应用
# appid="cli_a09151f62138900e"
# appsecret="yWU1huBPNi1cIoxuwIwdch1XBTkCrWjo"
#测试埋点租户
appid="cli_a4ce24d90d64500b"
appsecret="n2RCvvvceAkX4cnohMlgbdC0L5C5A71V"
#boe的自建租户的应用
# appid="cli_a3f6156913f8901b"
# appsecret="62ZkhYTnYNdNDrVF8hCXwgT5MC8t7nI6"


tokenJson={"app_id":appid,"app_secret":appsecret}
urlBoe='open.feishu-boe.cn'
urlOnline='open.feishu.cn'
urlStaging='open.feishu-pre.cn'


def getToken(url):
 r = requests.post(f'https://{url}/open-apis/auth/v3/tenant_access_token/internal', json=tokenJson,
                   headers={"Content-Type": "application/json"})
 print(r.json())
 return r.json().get("tenant_access_token")

token = getToken(urlStaging)


headers={
"Authorization":"Bearer "+token,
"Content-Type":"application/json"}

urlDIinfo=f"https://{urlStaging}/open-apis/hire/v1/applications/diversity_inclusions/search"

reqBody={
"application_ids":["7225089218715945272"]}
def genDIinfo():
    r=requests.post(url=urlDIinfo,headers=headers,json=reqBody)
    print(r)
    bodyJson=r.json()
    print("返回体:",bodyJson)
    print('\n')
    print("返回的header",r.headers)
    return bodyJson['code']



for i in range(20):
    t = threading.Thread(target=genDIinfo)
    t.start()