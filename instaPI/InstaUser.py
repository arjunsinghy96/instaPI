from Media import Media
from utils import get

class InstaUser:
    """
    Instagram user object.
    """
    def __init__(self, token, user_id=None):
        """
        :param token: access_token of the Instagram user
        :param user_id: Instagram user_id of the user
                        If the user_id is not provided the InstaUser will be
                        the owner of access_token.
                        If the user_id is provided the InstaUser will be the 
                        Instagram User corresponding to this user_id
        """
        self.token = token
        if user_id:
            self._data = get(token, '/users/' + user_id)
        else:
            self._data = get(token, '/users/self')
        self.id = self._data['id']
        self.bio = self._data['bio']
        self.username = self._data['username']
        self.full_name = self._data['full_name']
        self.profile_pic_url = self._data['profile_picture']
        self.website = self._data['website']
        self.follower_count = self._data['counts']['followed_by']
        self.follows_count = self._data['counts']['follows']
        self.media_count = self._data['counts']['media']

    def __repr__(self):
        """
        Representation of the InstaUser Object
        """
        ret = '<InstaUser object(id={}, username={}) at {}>'.format(
                    self.id,
                    self.username,
                    hex(id(self)))
        return ret

    def get_recent_media(self):
        """
        Yields a list of recent media objects for this user.
        """
        medialist = get(self.token,
                        '/users/{}/media/recent'.format(self.id))
        for data in medialist:
            media = Media(data)
            yield media
