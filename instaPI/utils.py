import requests
from exceptions import exceptions

BASE_URL = 'https://api.instagram.com/v1'

def get_response_data(method):
    """
    Extracts the value of 'data' key from the response of request.
    Raises appropriate error in case of any
    """
    def wrapper(*args, **kwargs):
        response = method(*args, **kwargs)
        if response.status_code == 404:
            raise exceptions['NotFoundError']()
        if response.status_code > 300:
            error = response.json()['meta']
            raise exceptions[error['error_type']](error['error_message'])
        data = response.json()['data']
        return data

    return wrapper


@get_response_data
def get(access_token, path, **kwargs):
    url =  '%s%s' % (BASE_URL, path)
    query_params = {
            'access_token': access_token
            }
    query_params.update(kwargs)
    response = requests.get(url, params=query_params)
    return response
