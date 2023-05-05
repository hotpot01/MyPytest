import json
items=[]
with open("respall") as f:
    line=f.readline()
    ss=line.split("page_token")
    print(ss,len(ss))
    print("分割线")
    print(ss[1])
    # try:
    #     items.append(linejson['data']['itmes'])
    # except:
    #     pass


