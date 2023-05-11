import logging
import uuid
import tqdm
import threading
from common.constants import appCons,urlCons
from common.utils import httpUtils
import requests

logging.basicConfig(level=logging.INFO)
#逻辑和数据都写在一起-->数据和逻辑分开，某些数据还可以在执行时进行修改


def createJR():

    reqBody={
    "short_code": str(uuid.uuid4()),
    "name": "test",
    "display_progress": 1,
    "head_count": 11,
    "recruitment_type_id": "101",
    "recruiter_id_list": [
        "c9bga4de"
    ],
    "customized_data_list": [
        {
            "object_id": "7179508244691175724",
            "value": "测试富文本"
        }
    ]
    }
    url=urlCons.boe_base_url
    token=httpUtils.getBoeToken(appId=appCons.boe_mingri_qa_all_appid,appSecret=appCons.boe_mingri_qa_all_appsecret)
    headers={"Authorization":token,"Content-Type":"application/json"}
    r=requests.post(f'{url}hire/v1/job_requirements',headers=headers,json=reqBody,params={"user_id_type":"user_id"})
    logging.info(r.text)

def taskone():
    for i in tqdm.trange(3000):
        createJR()


for i in range(3):
    t=threading.Thread(target=taskone)
    t.start()