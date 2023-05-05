import json
import requests
from faker import Faker
paraLs=[{'user_id_type': 'open_id',
  'consultant_id': 'ou_e88f64fa473fbea31d219d231aeaa184',
  'protect_create_time': '1670695587000',
  'protect_expire_time': '1680695587000',
  'talent_id': '7211021735322257675'},
 {'user_id_type': 'people_admin_id',
  'consultant_id': '6896810348297455112',
  'protect_create_time': '1670695587000',
  'protect_expire_time': '1680695587000',
  'talent_id': '7226633906735679803'},
 {'user_id_type': 'union_id',
  'consultant_id': 'on_49e1dcfe5776b031a6601eb4f0d1b559',
  'protect_create_time': '1670695587000',
  'protect_expire_time': '1680695587000',
  'talent_id': '7226633973790574907'},
 {'user_id_type': 'user_id',
  'consultant_id': 'a15dc8dc',
  'protect_create_time': '1670695587000',
  'protect_expire_time': '1680695587000',
  'talent_id': '7226633946070124811'},
 {'user_id_type': 'union_id',
  'consultant_id': 'on_49e1dcfe5776b031a6601eb4f0d1b559',
  'protect_create_time': '1680695587000',
  'protect_expire_time': '1670695587000',
  'talent_id': '7226634016895240451'}]

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
appid="cli_a09151f62138900e"
appsecret="yWU1huBPNi1cIoxuwIwdch1XBTkCrWjo"
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

token = getToken(urlOnline)


headers={
"Authorization":"Bearer "+token,
"Content-Type":"application/json"}
urlGenTalent=f"https://{urlOnline}/open-apis/hire/v1/talents/combined_create"

reqBody={
    "init_source_id": "1",
    "basic_info": {
      "name": "19200010029",
        "mobile":"19200010029",
        "mobile_country_code":"CN_1",
        "email":"19200010029@qq.com"
    }}
def genTalent(reqBody):
    r=requests.post(url=urlGenTalent,headers=headers,json=reqBody)
    bodyJson=r.json()
    return bodyJson['data']['talent_id']

genTalent(reqBody)
talent_ids=[]
fake = Faker(locale='zh_CN')
for i in range(len(paraLs)):
    reqBody.update({"basic_info": {"name":fake.name(),"mobile":fake.phone_number(),
                                   "mobile_country_code":"CN_1","email" :fake.email()}})
    talent_id=genTalent(reqBody)
    paraLs[i].update({"talent_id": talent_id})
print(paraLs)
with open("agency",'w') as f:
    json.dump(paraLs,f)
