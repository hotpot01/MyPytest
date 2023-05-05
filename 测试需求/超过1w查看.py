import requests
import json
import jsonschema

#获取token
#online的自建应用
# appid="cli_a3ee06d2463cd00d"
# appsecret="o9HuYTAAT8ugwYLBUZ33cceqWZpfCRHJ"
#boe的自建应用
appid="cli_a3d5d192aff8d01b"
appsecret="LexA85Jf2CypkhKWzBEqCcnbGfobjdSk"
#staging的自建应用
# appid="cli_a09151f62138900e"
# appsecret="yWU1huBPNi1cIoxuwIwdch1XBTkCrWjo"

tokenJson={"app_id":appid,"app_secret":appsecret}
urlBoe='open.feishu-boe.cn'
urlOnline='open.feishu.cn'
urlStaging='open.feishu-pre.cn'
def getToken(url):
    r=requests.post(f'https://{urlBoe}/open-apis/auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
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
"x-tt-atsx-openapi":"apix",
"x-tt-env":"boe_feat_job_openapi_use_searc"}

urlGetJob="https://"+urlBoe+"/open-apis/hire/v1/jobs"

#需要把上个请求返回的page_token,放到下一个请求的header中
#每次返回的数据需要记录
#每次返回需要加logid
items=[]
resp=[]
print("开始测试")
def getJobList(page_token):
    r=requests.get(url=urlGetJob,headers=headers,params={"page_size":20,"page_token":page_token})
    bodyjson=r.json()
    bodyjson.update({"logid":r.headers['X-Tt-Logid']})
    resp.append(bodyjson)
    print(bodyjson)
    try:
        if bodyjson['data']['has_more']==True:
            page_token=bodyjson['data']['page_token']
            # print(bodyjson['data']['items'])
            items.append(bodyjson['data']['items'])
            getJobList(page_token)
        else:
            print(bodyjson['data']['items'])
            items.append(bodyjson['data']['items'])
    except:
        raise


getJobList("")
print("all resp")
print(resp)
# print(items,len(items))
# with open('totalresp','w') as f:
#     json.dump(resp,f)