class test_data:
    '''Service URL'''
    SERVICE_URL = "https://reqres.in"

    '''GET API end point'''
    API_GetSingleUsers = "/api/users/2"

    '''GET SINGLE USER NOT FOUND end point'''
    API_GetSingleUserNotFound = "/api/users/23"

    '''POST API end point + Payload'''
    API_PostCreate = "/api/users"
    DATA_PostCreate = {"name": "morpheus", "job": "leader"}

    '''PUT API end point + Payload'''
    API_PutUpdate = "/api/users/2"
    DATA_PutUpdate = {"name": "praveen", "job": "QA expert"}

    '''DELETE API end point'''
    API_Delete = "/api/users/1"

    '''STATUS CODE'''
    STATUS_OK_200 = 200
    STATUS_CREATED_201 = 201
    STATUS_DELETE_204 = 204

    STATUS_NOT_FOUND_404 = 404

    STATUS_NOT_FOUND_500 = 500
