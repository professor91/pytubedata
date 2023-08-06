"""
pytubedata.data_models.comment

This module contains data model class for `comments` endpoint of YouTube Data API

Classes:
    CommentData: Represents the API response for the 'comments' endpoint.
"""


class CommentData:
    """
    Represents the API response for the 'comments' endpoint.
    """
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data['id']

    @property
    def author_name(self) -> str:
        return self._data['snippet']['authorDisplayName']

    @property
    def author_profile_image_url(self) -> str:
        return self._data['snippet']['authorProfileImageUrl']

    @property
    def author_channel_url(self) -> str:
        return self._data['snippet']['authorChannelUrl']

    @property
    def author_channel_id(self) -> str:
        return self._data["snippet"]["authorChannelId"]["value"]

    @property
    def text(self) -> str:
        return self._data["snippet"]["textDisplay"]

    @property
    def text_original(self) -> str:
        return self._data['snippet']['textOriginal']

    @property
    def published_at(self) -> str:
        return self._data["snippet"]["publishedAt"]

    @property
    def updated_at(self) -> str:
        return self._data['snippet']['updatedAt']

    @property
    def can_rate(self) -> bool:
        return self._data['snippet']['canRate']

    @property
    def likes(self) -> int:
        return self._data['snippet']['likeCount']
