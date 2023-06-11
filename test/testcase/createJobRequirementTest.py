from APIs.hireConfigs.jobRequirementService import jobRequirement
from common.constants import appCons, urlCons
from common.utils import httpUtils
import json
import os
if __name__ == '__main__':
    dir_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    # print((os.path.dirname(os.path.dirname(__file__))))
    datapath=dir_path+r"\testdata\JrCreateDataonline.json"
    with open(datapath,encoding="utf-8") as f:
        dataJson = json.load(f)
    url = urlCons.online_base_url
    createJob = jobRequirement.CreateJobRequirement(param={"user_id_type":"user_id"},
                                                    req_body=dataJson["createJobRequirement"]["in"]["reqBody"],
                                                    headers=httpUtils.getOnlineHeader(),
                                                    url=url + "hire/v1/job_requirements")
    r = createJob.post_request()
    print(r.text, "\n", r.headers["X-Tt-Logid"])
