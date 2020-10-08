import requests
import json
import pytest

url = "http://api.zippopotam.us"
params = "/IN/110001"

response = requests.get(url + params)
res_code = response.status_code
print(res_code)
response_body = response.json()
#prints in JSON format
print(json.dumps(response_body, indent=4))
import ipdb; ipdb.set_trace()
#print(response.headers)

def test_get_api():
    response = requests.get("http://api.zippopotam.us/IN/110001")
    print(response)
    print(response.headers)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'

    response_body = response.json()
    assert response_body['country'] == 'India'
    assert response_body['post code'] == '110001'
    assert response_body['places'][18]['place name'] == 'Shastri Bhawan'


