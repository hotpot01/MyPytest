import logging
import uuid
import tqdm
import threading
from common.constants import appCons,urlCons
from common.utils import httpUtils
import requests
import json
import os

logging.basicConfig(level=logging.INFO)
#逻辑和数据都写在一起-->数据和逻辑分开，某些数据还可以在执行时进行修改

#测试数据的获取
basepath=os.path.dirname(os.path.dirname(__file__))
datapath=os.path.join(basepath,"testdata/JrCreateDataonline.json")
with open(datapath,"r") as f:
    reqBody=json.load(f)
def createJR():
    reqBody.update({"short_code":str(uuid.uuid4())})
    url=urlCons.online_base_url
    token=httpUtils.getOnlineToken(appId=appCons.online_mingri_rd_all_appid,appSecret=appCons.online_mingri_rd_all_appsecret)
    headers={"Authorization":token,"Content-Type":"application/json"}
    r=requests.post(f'{url}hire/v1/job_requirements',headers=headers,json=reqBody,params={"user_id_type":"user_id"})
    logging.info(r.text)

def creatMore():
    for i in tqdm.trange(2500):
        createJR()

for i in range(3):
    t=threading.Thread(target=creatMore)
    t.start()