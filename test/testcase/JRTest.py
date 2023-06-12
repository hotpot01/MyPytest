from APIs.hireConfigs.jobRequirementService import jobRequirement
from common.constants import appCons, urlCons
from common.utils import httpUtils
import json
import os


def test_creat_jr():
    dir_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # print((os.path.dirname(os.path.dirname(__file__))))
    datapath=dir_path+r"\testdata\JrCreateDataonline.json"
    with open(datapath,encoding="utf-8") as f:
        dataJson = json.load(f)
    url = urlCons.online_base_url
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


class JRtest():
    base_url=""

    def test_new(self):
        pass