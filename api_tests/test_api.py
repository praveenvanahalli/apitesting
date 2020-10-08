import pytest
from base1.conftest import get_api, post_api, put_api, delete_api
from config.config import test_data
import allure


# @pytest.mark.get
# @pytest.mark.usefixtures("get_api")



def test_api_get():
    resp = get_api()
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_OK_200
    assert resp_body["data"]["id"] == 2
    assert resp_body["data"]["email"] == "janet.weaver@reqres.in"
    assert resp_body["data"]["first_name"] == "Janet"
    assert resp_body["ad"]["company"] == "StatusCode Weekly"
    assert resp_body["ad"]["url"] == "http://statuscode.org/"


def test_api_post():
    resp = post_api()
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_CREATED_201
    assert resp_body["name"] == "morpheus"

def test_api_put():
    resp = put_api()
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_OK_200
    assert resp_body["name"] == "praveen"

def test_api_delete():
    resp = delete_api()
    assert (resp.status_code == test_data.STATUS_DELETE_204), "Status is not 204"
    #assert resp_body["name"] == []



