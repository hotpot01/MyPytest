from APIs.hireConfigs.jobRequirementService import jobRequirement
from common.constants import appCons, urlCons
from common.utils import httpUtils
import json

if __name__ == '__main__':
    with open("/Users/bytedance/testPyMy/test/testdata/JrCreateDataonline.json") as f:
        dataJson = json.load(f)
    url = urlCons.online_base_url
    createJob = jobRequirement.CreateJobRequirement(param="",
                                                    req_body=dataJson["createJobRequirement"]["in"]["reqBody"],
                                                    headers=httpUtils.getOnlineHeader(),
                                                    url=url + "hire/v1/job_requirements")
    r = createJob.post_request()
    print(r.text, "\n", r.headers["X-Tt-Logid"])
