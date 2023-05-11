import requests
import json
import uuid
import jsonschema
from faker import Faker
import random
from tqdm import trange
import threading
#使用参考 https://blog.csdn.net/yao2003365/article/details/126248425
fake=Faker("zh_CN")

# 获取token
# online的自建应用
# appid="cli_a3ee06d2463cd00d"
# appsecret="o9HuYTAAT8ugwYLBUZ33cceqWZpfCRHJ"
# boe公用的自建应用
# appid="cli_a3d5d192aff8d01b"
# appsecret="LexA85Jf2CypkhKWzBEqCcnbGfobjdSk"
# staging的自建应用
# appid="cli_a09151f62138900e"
# appsecret="yWU1huBPNi1cIoxuwIwdch1XBTkCrWjo"
# boe的自建租户的应用
appid="cli_a3f6156913f8901b"
appsecret="62ZkhYTnYNdNDrVF8hCXwgT5MC8t7nI6"


tokenJson={"app_id":appid,"app_secret":appsecret}
urlBoe='open.feishu-boe.cn'
urlOnline='open.feishu.cn'
urlStaging='open.feishu-pre.cn'
def getToken(url):
    r=requests.post(f'https://{urlBoe}/open-apis/auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
    print(r.json())
    return r.json().get("tenant_access_token")

token=getToken(urlOnline)

print(token)


headers={
"Authorization":"Bearer "+token,
"Content-Type":"application/json",
"x-tt-atsx-openapi":"apix"}

urlGetJob="https://"+urlBoe+"/open-apis/hire/v1/jobs"
urlCreatJob="https://open.feishu-boe.cn/open-apis/hire/v1/jobs/combined_create"
reqbody={
  "code": "11111",
  "expiry_time": 1696446309000,
  "address_id": "1234",
  "title": "111",
  "job_managers": {
    "recruiter_id": "ou_50fe86056ab869d400a474381bb6367f",
    "hiring_manager_id_list": [
      "ou_50fe86056ab869d400a474381bb6367f"
    ]
  },
  "job_process_id": "7163943657745189164",
  "process_type": 1,
  "department_id": "od-99469ab17567138708547b41111d97ce",
  "is_never_expired": False,
  "job_type_id": "6791698585114724616",
  "recruitment_type_id": "101"
}
#需要把上个请求返回的page_token,放到下一个请求的header中
#每次返回的数据需要记录
#每次返回需要加logid
items=[]
resp=[]
def creatJob():
    for i in trange(100):
        reqbody.update({"code":str(uuid.uuid4()),"title":str(uuid.uuid4())})
        r=requests.post(url=urlCreatJob,headers=headers,json=reqbody)
        print(r)
# t1=threading.Thread(target=creatJob())

for i in range(5):
    t=threading.Thread(target=creatJob)
    t.start()
