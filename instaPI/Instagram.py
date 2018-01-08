from InstaUser import InstaUser
from Media import Media
from utils import get

class Instagram:

    def __init__(self, token):
        """
        Construct Instagram object.

        :param token: String of Instagram Access Token
        """
        self.token = token
        self.user = None

    def get_user(self):
        """
        Create an InstaUser object associated with the token.
        
        :return: InstaUser object.
        """
        if not self.user:
            self.user = InstaUser(self.token)
        return self.user

    def get_recent_media_for_user(self, user_id=None):
        """
        Yields a list of recent media for given user
        :param user_id: User id for which recent media is to be fetched
                        If not provided the user for access token is used
        """
        if user_id:
            medialist = get(self.token,
                            '/users/{}/media/recent'.format(user_id))
        else:
            medialist = get(self.token,
                            '/users/self/media/recent')
        for data in medialist:
            media = Media(data)
            yield media
