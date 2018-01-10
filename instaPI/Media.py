class Media:

    def __init__(self, media_data=None):
        """
        :param token: String of intagram access_token.
        """
        self._data = media_data
        #TODO: Represent some fields as objects
        self.id = self._data['id']
        self.type = self._data['type']
        self.filter = self._data['filter']
        self.tags = self._data['tags']
        self.caption = self._data['caption']
        self.likes = self._data['likes']['count']
        self.comments = self._data['comments']['count']
        self.link = self._data['link']
        self.created_time = self._data['created_time']
        self.user = self._data['user']
        self.location = self._data['location']
        self.images = self._data['images']

    def __repr__(self):
        """
        Represnetatin of the Media Object
        """
        ret = '<Media object(id={}, type={}, link={} at {}'.format(
                    self.id,
                    self.type,
                    self.link,
                    hex(id(self)))
        return ret

    @property
    def thumbnail(self):
        """
        Returns thumbnail url of Media
        """
        return self.images['thumbnail']['url']

    @property
    def low_resolution(self):
        """
        Returns low resolution image url
        """
        return self.images['low_resolution']['url']

    @property
    def standard_resolution(self):
        """
        Returns standard resolution url of image.
        """
        return self.images['standard_resolution']['url']
