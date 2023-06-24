import pytest
import pathlib
from APIs.hireConfigs.jobRequirementService import jobRequirement
from common.constants import appCons, urlCons
from common.utils import httpUtils
import json
import hashlib
import os

url=urlCons.online_base_url
def test_creat_jr():
    file=pathlib.Path(__file__)
    datapath=file.resolve().parents[1].joinpath("testdata/JrCreateDataonline.json")
    with open(datapath,encoding="utf-8") as f:
        dataJson = json.load(f)
    # url = urlCons.online_base_url
    createJob = jobRequirement.CreateJobRequirement(param={"user_id_type":"user_id"},
                                                    req_body=dataJson["createJobRequirement"]["in"]["reqBody"],
                                                    headers=httpUtils.getOnlineHeader(),
                                                    base_url=url)
    r = createJob.post_request()
    print(r.text, "\n", r.headers["X-Tt-Logid"])
def test_get_jr():
    url = urlCons.online_base_url
    getJob = jobRequirement.getJobRequirement(param={"user_id_type":"user_id"},
                                                    headers=httpUtils.getOnlineHeader(),
                                                    base_url=url)
    r = getJob.post_request()
    print(r.text, "\n", r.headers["X-Tt-Logid"])

def test_get_jrList():
    url = urlCons.online_base_url
    getJob = jobRequirement.getJobRequirementList(param={"user_id_type":"user_id"},
                                                    headers=httpUtils.getOnlineHeader(),
                                                    base_url=url)
    r = getJob.post_request()
    print(r.text, "\n", r.headers["X-Tt-Logid"])


#学习使用参数化，这个参数的规则是，目前看就是简单的传参，并不会进行组合
#参数化后，测试用例需要传入对应的参数
@pytest.mark.parametrize('passwd',
                      ['123456',
                       'abcdefdfs',
                       'as52345fasdf4'])
def test_passwd_length(passwd):
    assert len(passwd) >= 8

@pytest.mark.parametrize("user,passwd",[("1","2"),("good","bad")])
def test_user_passwd(user,passwd):
    print(user,passwd)

@pytest.mark.parametrize('user, passwd',
                         [('jack', 'abcdefgh'),
                          ('tom', 'a123456a')],ids=['testJack',"testTom"])
def test_passwd_md5(user, passwd):
    db = {
        'jack': 'e8dc4081b13434b45189a720b77b6818',
        'tom': '1702a132e769a623c1adb78353fc9503'
    }
    assert hashlib.md5(passwd.encode()).hexdigest() == db[user]
#实现参数组合，笛卡尔积
@pytest.mark.parametrize("a",[1,2])
@pytest.mark.parametrize("b",[3,4])
@pytest.mark.parametrize("c",[1,2,3,4])
def test_ab(a,b,c):
    print(a,b,c)



# Todo  1.不可能同一个接口，因为测试数据不同，而写多条用例 2. 断言的时候怎么处理，不同的数据会有不同的断言 3.需要做到什么粒度
# 分两大类逻辑测试（正向，方向，边界）和结构测试（返回结构体），后面的性能(qps)和安全测试，放在一边另说

#用例的分组执行
#content of test_param.py
# coding=utf-8
import pytest

#利用pytest.param添加,粒度更细，可以针对单条用例进行定制
@pytest.mark.parametrize("a,b,expected",
    [(4,2,1), pytest.param(9,3,6, marks=pytest.mark.xfail,id="expect fail")
     ,pytest.param(5,3,1,marks=[pytest.mark.first,pytest.mark.xfail],id="test3")],
)
def test_diff_v3(a, b, expected):
    diff = a - b
    assert diff == expected

class TestFR():
    base_url=""

    def test_new(self):
        pass