import requests
from conftest import get_api
from config.config import test_data

SERVICE_URL = "http://reqres.in"
API_GetSingleUsers = "/api/users/2"
API_PostCreate = "/api/users"
url = "http://reqres.in/api/users/2"

#url = SERVICE_URL + API_GetSingleUsers


# def test_01():
#     response = requests.get(url)
#     resp_body = response.json()
#     print(json.dumps(resp_body, indent=4))
#     assert response.status_code == 200


def test_02():
    resp = get_api()
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_CREATED_201
    print(len(resp_body["data"]))
    assert resp_body["data"]["first_name"] == "Janet"


def test_api_delete():
    resp = requests.delete(url)
    print(resp.status_code)
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_DELETE_204

