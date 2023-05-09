import requests

def getOnlineToken():
    r=requests.post(f'https://{url}/open-apis/auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
    print(r.json())
    return r.json().get("tenant_access_token")
def getStagingToken():
    pass
def getBoeToken():
    pass

def getPreHeader():
    pass