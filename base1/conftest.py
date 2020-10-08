import pytest
import requests

from config.config import test_data

'''Validate GET API'''
def get_api():
    response = requests.get(test_data.SERVICE_URL + test_data.API_GetSingleUsers)
    return response


'''Validate POST API'''
def post_api():
    response = requests.post(test_data.SERVICE_URL + test_data.API_PostCreate, data=test_data.DATA_PostCreate)
    return response

'''Validate PUT API'''
def put_api():
    response = requests.put(test_data.SERVICE_URL + test_data.API_PutUpdate, data=test_data.DATA_PutUpdate)
    return response

'''Validate DELETE API'''
def delete_api():
    response = requests.delete(test_data.SERVICE_URL + test_data.API_Delete)
    return response

