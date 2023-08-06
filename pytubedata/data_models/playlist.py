"""
pytubedata.data_models.playlist

This module contains data model class for `playlists` endpoint of YouTube Data API

Classes:
    PlaylistData: Represents the API response for the 'playlists' endpoint.
"""


class PlaylistData:
    """
    Represents the API response for the 'playlists' endpoint.
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
    def published_at(self) -> str:
        return self._data['snippet']['publishedAt']

    @property
    def thumbnail_url(self) -> str:
        return self._data["snippet"]["thumbnails"]["default"]["url"]

    @property
    def videos_count(self) -> int:
        return self._data['contentDetails']['itemCount']
