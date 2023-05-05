import requests
import jsonschema

schema={}
url="http://example.org"
res=requests.get(url)

jsonschema.validate(res.json(),schema)
