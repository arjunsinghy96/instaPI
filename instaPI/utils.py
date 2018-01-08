import requests

BASE_URL = 'https://api.instagram.com/v1'

def get_response_data(method):
    """
    Extracts the value of 'data' key from the response of request.
    Raises appropriate error in case of any
    """
    def wrapper(*args, **kwargs):
        response = method(*args, **kwargs)
        data = response.json()['data']
        return data

    return wrapper


@get_response_data
def get(access_token, path):
    url =  '%s%s?access_token=%s' % (BASE_URL, path, access_token)
    response = requests.get(url)
    return response
