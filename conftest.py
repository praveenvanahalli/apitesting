import pytest
import requests

from config.config import test_data

'''Validate GET API'''
@pytest.fixture()
def get_api():
    #self.endpoint = endpoint
    response = requests.get(test_data.SERVICE_URL + test_data.API_GetSingleUsers)
    return response


'''Validate POST API'''
@pytest.fixture()
def post_api():
    response = requests.post(test_data.SERVICE_URL + test_data.API_PostCreate, data=test_data.DATA_PostCreate)
    return response


'''Validate PUT API'''
@pytest.fixture()
def put_api():
    response = requests.put(test_data.SERVICE_URL + test_data.API_PutUpdate, data=test_data.DATA_PutUpdate)
    return response


'''Validate DELETE API'''
@pytest.fixture()
def delete_api():
    response = requests.delete(test_data.SERVICE_URL + test_data.API_Delete)
    return response

'''Validate GET - Not found user API'''
@pytest.fixture()
def get_not_found_user():
    response = requests.get(test_data.SERVICE_URL + test_data.API_GetSingleUserNotFound)
    return response


