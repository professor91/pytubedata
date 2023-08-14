"""
pytubedata.data_models.channel

This module contains data model class for `channels` endpoint of YouTube Data API

Classes:
    ChannelData: Represents the API response for the 'channels' endpoint.
"""


class ChannelData:
    """
    Represents the API response for the 'channels' endpoint.
    """
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data['id']

    @property
    def title(self) -> str:
        return self._data['snippet']['title']

    @property
    def description(self) -> str:
        return self._data['snippet']['description']

    @property
    def published_at(self) -> str:
        return self._data['snippet']['publishedAt']

    @property
    def country(self) -> str:
        return self._data['snippet']['country']

    @property
    def custom_url(self) -> str:
        return self._data['snippet'].get('customUrl', None)

    @property
    def subscribers(self) -> int:
        return self._data['statistics']['subscriberCount']

    @property
    def videos(self) -> int:
        return self._data['statistics']['videoCount']

    @property
    def views(self) -> int:
        return self._data['statistics']['viewCount']
