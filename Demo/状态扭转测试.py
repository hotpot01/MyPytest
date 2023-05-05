import requests
import json
import copy

# 收获，数据列表操作时，如果需要保留源列表的结构，要进行深拷贝
# 对python 内置数据结构-列表的熟悉，哪些时inplace的替换，哪些不是
lsAllPath=[]
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
 # 如果当前节点为终止节点，则输出当前遍历路径 print(path)
        lsAllPath.append(path)
        # print(path)
        return path
    for node in graph[start]:
        if node not in path:
            dfs_paths(graph, node, end, path)

graph = {
2: [3,4,5],
3: [2],
4: [3,6],
5: [2],
6: [7,8,9],
7: [8],
8:[7,2],
9:[2]
}
pathAll=[]
for i in range(2,10):
    for j in range(2,10):
        pathAll.append(dfs_paths(graph,i,j))

# print(lsAllPath)
print("所有路径的长度：",len(lsAllPath))

#将path进行分组
ddgroup={}
for i in range(2,10):
    lstemp=[]
    for item in lsAllPath:
#         print(item)
        if item[0]==i:
            lstemp.append(item)
            ddgroup[i]=lstemp
#把其他的路径，拼接到以审批中开始的路径后面
dstart2=ddgroup[2]
dictadd={}
for j in dstart2:
    for i in range(3,10):
        ls=[]
        for item in ddgroup[i]:
            if j[-1]==item[0]:
                temp=j+item
                ls.append(temp)
                dictadd[i]=ls
#对拼接处，进行去重处理
for i in range(3,10):
    for item in dictadd[i]:
        item.remove(i)
#对拼接的path,进行路径子集的判断
# print(dictadd)
with open("dictdd.json",'w') as f:
    json.dump(dictadd,f)

#set会把重复项去掉，需要自己写一个函数来判断是否是子集，如果短列表的所有位置上的值和长列表都对上了，那就把这个列表去掉
#列表相等时的情况需要考虑到（列表长度相等，不代表没有重复的元素）
#是子集就不加入，不是子集才加入
def isSubset(longls,shortls):
    lenlong=len(longls)
    lenshort=len(shortls)
    if lenlong<lenshort:
        return False
    if lenlong==lenshort:
        tmep=0
        for i in range(lenshort):
            if shortls[i]==longls[i]:
                tmep+=1
        if tmep==lenshort:
            return True
        else:
            return False
    if lenlong>lenshort:
        tmep=0
        for i in range(lenshort):
            if shortls[i]==longls[i]:
                tmep+=1
        if tmep==lenshort:
            return True
        else:
            return False

# #自己和自己还需要比较，进行去重，这里不能用到隐形的条件：更长的列表不会是更短列表的子集
# lsUpper=set()
# for i in range(9,2,-1):
#     for j in range(9,2,-1):
#         for k in range(len(dictadd[i])):
#             for m in range(len(dictadd[j])):
#                 if subset(dictadd[i][k],dictadd[j][m]):
#                     lsUpper.add(tuple(dictadd[i][k]))
# print(lsUpper)
# print(len(lsUpper))

#长度排序之后，再进行遍历：1.先要把分组去掉（解包），然后去重 2.是子集就不加入，不是子集才加入
newls=list(dictadd.values())
nn=[]
for item in newls:
    for i in item:
        nn.append(i)
ns=sorted(nn,key=lambda x:len(x))
lsinit=[ns[-1]]
for item in ns:
    if isSubset(lsinit[0],item):
        pass
    else:
        lsinit.append(item)

tosave=copy.deepcopy(lsinit)

for i in range(len(lsinit)-1,0,-1):
    for j in range(i-1,0,-1):
        if isSubset(lsinit[i],lsinit[j]):
            try:
                tosave.remove(lsinit[j])
            except:
                pass

print("最后的路径",tosave)
print("最后路径的长度",len(tosave))
with open("longpath",'w') as f:
    for item in tosave:
        f.write(str(item))
        f.write("\n")


#进行请求,状态扭转
#获取token
appid="cli_a3ee06d2463cd00d"
appsecret="o9HuYTAAT8ugwYLBUZ33cceqWZpfCRHJ"
tokenJson={"app_id":appid,"app_secret":appsecret}
urlBoe='open.feishu-boe.cn'
urlOnline='open.feishu.cn'
def getToken(url):
    r=requests.post(f'https://{url}/open-apis/auth/v3/tenant_access_token/internal',json=tokenJson,headers={"Content-Type":"application/json"})
    print(r.json())
    return r.json().get("tenant_access_token")
offerID="7218772878199326987"
token=getToken(urlOnline)
# token='t-g10246jh4XFHSIDWHT7KSPVDMGUILWEVFKU5LCD5'
print(token)
url=f"https://{urlOnline}/open-apis/hire/v1/offers/{offerID}/offer_status"

headers={
"Authorization":"Bearer "+token,
"Content-Type":"application/json"}
reqBody={
    "offer_status": 2,
    "expiration_date": "2023-08-09",
    "termination_reason_id_list": [
        "721515283"
    ],
    "termination_reason_note": "no"
}

def offerStatus(status):
    reqBody.update({"offer_status": status})
    r=requests.patch(url=url,headers=headers,json=reqBody)
    print(reqBody)
    print(r.json())
for item in tosave[0]:
    offerStatus(item)

#最长的路径+回到最初的状态,所有路径回到2,或者创建22个offer

for group in tosave:
    for path in group:
        offerStatus(path)