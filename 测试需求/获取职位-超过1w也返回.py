import requests
import json
import jsonschema

#获取token
#online的自建应用
appid="cli_a3ee06d2463cd00d"
appsecret="o9HuYTAAT8ugwYLBUZ33cceqWZpfCRHJ"
#boe的自建应用
# appid="cli_a3d5d192aff8d01b"
# appsecret="LexA85Jf2CypkhKWzBEqCcnbGfobjdSk"
#staging的自建应用
# appid="cli_a09151f62138900e"
# appsecret="yWU1huBPNi1cIoxuwIwdch1XBTkCrWjo"
#自己租户的boe
# appid="cli_a3f6156913f8901b"
# appsecret="62ZkhYTnYNdNDrVF8hCXwgT5MC8t7nI6"

tokenJson={"app_id":appid,"app_secret":appsecret}
urlBoe='open.feishu-boe.cn'
urlOnline='open.feishu.cn'
urlStaging='open.feishu-pre.cn'
def getToken(url):
    r=requests.post(f'https://{urlOnline}/open-apis/auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
    print(r.json())
    return r.json().get("tenant_access_token")
offerID="7218772878199326987"
token=getToken(urlOnline)
# token='t-g10246jh4XFHSIDWHT7KSPVDMGUILWEVFKU5LCD5'
print(token)
url=f"https://{urlOnline}/open-apis/hire/v1/offers/{offerID}/offer_status"

headers={
"Authorization":"Bearer "+token,
"Content-Type":"application/json",
"x-tt-atsx-openapi":"apix-pre",
"x-candidate-pre": "pre",
"Atsx-Env-Release": "PreRelease"}

urlGetJob="https://"+urlOnline+"/open-apis/hire/v1/jobs"

#需要把上个请求返回的page_token,放到下一个请求的header中
#每次返回的数据需要记录
#每次返回需要加logid
items=[]
resp=[]
f=open("respallonline","w+")
def getJobList(page_token):
    r=requests.get(url=urlGetJob,headers=headers,params={"page_size":20,"page_token":page_token})
    print(r.text)
    f.write(r.text)
    f.write("\n")
    bodyjson=r.json()
    bodyjson.update({"logid":r.headers['X-Tt-Logid']})
    print(bodyjson)
    return bodyjson

page_token=""
while True:
    bodyjson=getJobList(page_token)
    page_token=bodyjson['data']['page_token']
    if bodyjson['data']['has_more']==False:
        break
    else:
        getJobList(page_token)

