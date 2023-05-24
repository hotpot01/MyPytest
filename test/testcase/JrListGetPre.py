import json
import logging
import uuid
import tqdm
import threading
from common.constants import appCons,urlCons
from common.utils import httpUtils
import requests


Preheader={"x-candidate-pre":"pre",
"Atsx-Env-Release":"PreRelease",
"x-tt-atsx-openapi":"oapi-pre"}
def getJrList(page_token):
    url=urlCons.online_base_url
    token=httpUtils.getOnlineToken(appId=appCons.online_mingri_qa_all_appid,appSecret=appCons.online_mingri__qa_all_appsecret)
    headers={"Authorization":token,"Content-Type":"application/json"}
    headers.update(Preheader)
    r=requests.get(f'{url}hire/v1/job_requirements',headers=headers,
                    params={"user_id_type":"user_id","create_time_begin":"1603561600123","page_size":20,"page_token":page_token})
    logging.info(r.text)
    bodyJson=r.json()
    # print(bodyJson["data"]["page_token"])
    return bodyJson

page_token=""
i=0
f=open("getjrlist2","w+")
while True:
    try:
        bodyjson=getJrList(page_token)
        # #把获取的数据，写到文件中
        # f.write()
        # f.write(json.dumps(bodyjson))
        # f.write("\n")
        print(f"第几次执行:{i}，和page_token:{page_token},响应体{bodyjson}")
        page_token=bodyjson['data']['page_token']
        i=i+1
        if bodyjson['data']['has_more']==False:
            f.close()
            break
        if bodyjson['code']!=0:
            break
        else:
            getJrList(page_token)
    except:
        f.close()