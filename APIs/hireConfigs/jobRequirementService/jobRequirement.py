import requests

class CreateJobRequirement:
    def __init__(self, param, req_body, headers, base_url,path="hire/v1/job_requirements"):
        self.url = base_url
        self.params = param
        self.req_body = req_body
        self.headers = headers
        self.path=path

    def post_request(self):
        response = requests.post(url=self.url+self.path, params=self.params, json=self.req_body, headers=self.headers)
        return response

# # 使用类创建一个对象
# job_req = CreateJobRequirement(param, req_body, headers)
#
# # 调用 post_request 方法发送请求
# response = job_req.post_request()
#
# # 处理响应
# print(response.status_code)
# print(response.json())
