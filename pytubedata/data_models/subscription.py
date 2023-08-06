"""
pytubedata.data_models.subscription

This module contains data model class for `subscriptions` endpoint of YouTube Data API

Classes:
    SubscriptionData: Represents the API response for the 'subscriptions' endpoint.
"""


class SubscriptionData:
    """
    Represents the API response for the 'subscriptions' endpoint.
    """
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data['id']

    @property
    def channel_id(self) -> str:
        return self._data['snippet']['channelId']

    @property
    def channel_title(self) -> str:
        return self._data['snippet']['title']

    @property
    def channel_description(self) -> str:
        return self._data['snippet']['description']

    @property
    def subscribed_on(self) -> str:
        return self._data['snippet']['publishedAt']

    @property
    def videos_count(self) -> int:
        return self._data['contentDetails']['totalItemCount']

    @property
    def new_videos_count(self) -> int:
        return self._data['contentDetails']['newItemCount']
