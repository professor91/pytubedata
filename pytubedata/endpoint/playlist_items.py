"""
pytubedata.playlist_items

This module provides a convenient interface to interact with the 'playlistItems' endpoint of the YouTube Data API.
It allows users to retrieve videos of a YouTube playlist given their ID.

Classes:
    PlaylistItems: Encapsulates functions to interact with the 'playlists' endpoint of the YouTube Data API.
"""
from pytubedata.playlist_item import PlaylistItem

from pytubedata.config import ENDPOINT_PLAYLIST_ITEM_PARAM_PART


class PlaylistItems:
    """
    Encapsulates functions to interact with the `playlistItems` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_playlists_by_channel(channel_id: str, **kwargs) -> list:
            Get playlists of a specific channel.

    Raises:
        ValueError: If the playlist_id(s) are invalid or missing.
    """
    ENDPOINT = 'playlistItems'

    def __init__(self, api_request: object):
        """
        Initializes the PlaylistItems object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.
        """
        self.api_request = api_request

    def get_playlist_items(self, playlist_id: str, **kwargs) -> list[PlaylistItem]:
        """
        Get videos of a playlist given its id.

        Args:
            playlist_id (str): The id of the YouTube playlist which videos to fetch.

            kwargs: Check the official documentation for additional parameter to customize the request

        Returns:
            list: The list of PlaylistData object containing the details of the fetched playlists.
        """
        params = {
            "part": ENDPOINT_PLAYLIST_ITEM_PARAM_PART,
            "playlistId": playlist_id,
        }
        params.update(kwargs)

        response: dict = self.api_request.make_request(PlaylistItems.ENDPOINT, params=params)

        return [PlaylistItem(item, self.api_request) for item in response["items"]]
