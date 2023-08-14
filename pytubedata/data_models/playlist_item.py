"""
pytubedata.data_models.playlist_item

This module contains data model class for `playlistItems` endpoint of YouTube Data API

Classes:
    PlaylistItemData: Represents the API response for the 'playlistItems' endpoint.
"""


class PlaylistItemData:
    """
    Represents the API response for the 'playlistItems' endpoint.
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
    def channel_id(self) -> str:
        return self._data['snippet']['channelId']

    @property
    def channel_title(self) -> str:
        return self._data['snippet']['channelTitle']

    @property
    def owner_channel_id(self) -> str:
        return self._data['snippet']['videoOwnerChannelId']

    @property
    def owner_channel_title(self) -> str:
        return self._data['snippet']['videoOwnerChannelTitle']

    @property
    def added_at(self) -> str:
        return self._data['snippet']['publishedAt']

    @property
    def video_id(self) -> str:
        return self._data['snippet']['resourceId']['videoId']
