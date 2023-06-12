import requests

class CreateJobRequirement:
    def __init__(self, param, req_body, headers,base_url,path="hire/v1/job_requirements"):
        self.url = base_url+path
        self.params = param
        self.req_body = req_body
        self.headers = headers
        self.path=path

    def post_request(self):
        response = requests.post(url=self.url+self.path, params=self.params, json=self.req_body, headers=self.headers)
        return response
class getJobRequirement:
    def __init__(self, param,headers,base_url,path="hire/job_requirements/search"):
        self.url = base_url+path
        self.params = param
        self.headers = headers

    def post_request(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        return response

class getJobRequirementList:
    def __init__(self, param,headers,base_url,path="hire/v1/job_requirements"):
        self.url = base_url+path
        self.params = param
        self.headers = headers

    def post_request(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        return response
def deletJobRequirement():
    pass