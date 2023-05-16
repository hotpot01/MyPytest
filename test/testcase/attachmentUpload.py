import json
import logging
import uuid
import tqdm
import threading
from common.constants import appCons,urlCons
from common.utils import httpUtils
import requests
from requests_toolbelt import MultipartEncoder

logging.basicConfig(level=logging.INFO)
f=open("/Users/bytedance/testPyMy/test/testdata/newfiles","rb")
data = MultipartEncoder(fields={'content':("None",f)})
# requests.post(url=url,data=data,headers={ 'Content-Type': data.content_type})
def attachmentUpload():
    url=urlCons.online_base_url
    token=httpUtils.getOnlineToken(appId=appCons.online_mingri_qa_all_appid,appSecret=appCons.online_mingri__qa_all_appsecret)
    headers={"Authorization":token,
             # "Content-Type":"application/json",
             # "Content-Type": "multipart/form-data",
             # 'Content-Type': data.content_type
             }
    files={"file":("content",f,"multipart/form-data")}
    r=requests.post(f'{url}hire/v1/attachments',headers=headers,
                    # data=data
                    files={"content":f}
                    )
    logging.info(r.text)
    bodyJson=r.json()
    # print(bodyJson["data"]["page_token"])
    return bodyJson

attachmentUpload()