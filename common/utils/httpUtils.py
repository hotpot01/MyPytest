import requests
import logging
from common.constants import appCons,urlCons

#主要是还有租户的信息

def getOnlineToken(appId,appSecret):
    url=urlCons.online_base_url
    tokenJson={
        "app_id":appId,
        "app_secret":appSecret
    }
    r=requests.post(f'{url}auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
    logging.info(r.json())
    return "Bearer "+r.json().get("tenant_access_token")

def getBoeToken(appId,appSecret):
    url=urlCons.boe_base_url
    tokenJson={
        "app_id":appId,
        "app_secret":appSecret
    }
    r=requests.post(f'{url}auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
    logging.info(r.json())
    return "Bearer "+r.json().get("tenant_access_token")
def getOnlineHeader():
    pass
def getPreHeader():
    pass