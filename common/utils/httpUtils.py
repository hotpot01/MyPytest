import requests
import logging
from common.constants import appCons, urlCons


# 主要是还有租户的信息

def getOnlineToken(appId, appSecret):
    url = urlCons.online_base_url
    tokenJson = {
        "app_id": appId,
        "app_secret": appSecret
    }
    r = requests.post(f'{url}auth/v3/tenant_access_token/internal', json=tokenJson,
                      headers={"Content-Type": "application/json"})
    logging.info(r.json())
    return "Bearer " + r.json().get("tenant_access_token")


def getBoeToken(appId, appSecret):
    url = urlCons.boe_base_url
    tokenJson = {
        "app_id": appId,
        "app_secret": appSecret
    }
    r = requests.post(f'{url}auth/v3/tenant_access_token/internal', json=tokenJson,
                      headers={"Content-Type": "application/json"})
    logging.info(r.json())
    return "Bearer " + r.json().get("tenant_access_token")


def getOnlineHeader(appId=appCons.online_mingri_rd_all_appid, appSecret=appCons.online_mingri_rd_all_appsecret, **kwargs):
    kw = kwargs
    headers = {
        "Authorization": getOnlineToken(appId, appSecret),
        "Content-Type": "application/json",
    }
    headers.update(kw)
    return headers


def getPreHeader():
    pass

if __name__ == '__main__':
    h = getOnlineHeader(appCons.online_mingri_rd_all_appid
                        , appCons.online_mingri_rd_all_appsecret, **{"env": "new", "tok": "1"})
    print(type(h))
