from config.config import test_data

'''Validate GET API'''
def test_api_get(get_api):
    resp = get_api
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_OK_200
    assert resp_body["data"]["id"] == 2
    assert resp_body["data"]["email"] == "janet.weaver@reqres.in"
    assert resp_body["data"]["first_name"] == "Janet"
    assert resp_body["ad"]["company"] == "StatusCode Weekly"
    assert resp_body["ad"]["url"] == "http://statuscode.org/"


'''Validate POST API'''


def test_api_post(post_api):
    resp = post_api
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_CREATED_201
    assert resp_body["name"] == "morpheus"


'''Validate PUT API'''


def test_api_put(put_api):
    resp = put_api
    resp_body = resp.json()
    assert resp.status_code == test_data.STATUS_OK_200
    assert resp_body["name"] == "praveen"


'''Validate DELETE API'''


def test_api_delete(delete_api):
    resp = delete_api
    assert (resp.status_code == test_data.STATUS_DELETE_204), "Status is not 204"


'''Validate GET not found user API'''


def test_api_get_not_found(get_not_found_user):
    resp = get_not_found_user
    assert resp.status_code == test_data.STATUS_NOT_FOUND_404

