import json
import logging
import uuid
import tqdm
import threading
from common.constants import appCons,urlCons
from common.utils import httpUtils
import requests
from requests_toolbelt import MultipartEncoder
import threading



def authRole():
    reqBody={
    "role_list": [
    {
      "role_id": "999"
    }
  ]
}
    url="https://open.feishu-pre.cn/open-apis/hire/v1/users/ou_db5bbc338216cd10f1892c86d7d9f44e/authorize"
    headers={
        "Authorization":"Bearer t-g1045i9DPXOBOHHNTQ2FPSTRWM4K45LB3VBEFERD",
        "Content-Type":"application/json"
    }
    r=requests.post(url=url,json=reqBody,headers=headers)
    print(r.json())


for i in range(20):
    t=threading.Thread(target=authRole)
    t.start()
