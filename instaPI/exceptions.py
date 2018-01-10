class OAuthPermissionError(Exception):
    """
    Represents OAuthPermissionsExeption of Instagram.
    OAuthPermissionsException is raised when the token is not approved to
    access the resource.
    """
    def __init__(self, message):
        self.message = message

class NotFoundError(Exception):
    """
    Represents 404 Not Found
    """
    def __init__(self):
        self.message = 'The requested resource does not exist'


class APINotAllowedError(Exception):
    """
    Repersents APINotAllowedError of Instagram.
    """
    def __init__(self, message):
        self.message = message

exceptions = {
        'OAuthPermissionsException': OAuthPermissionError,
        'APINotAllowedError': APINotAllowedError,
        'NotFoundError': NotFoundError,
        }
