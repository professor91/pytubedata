"""
pytubedata.playlists

This module provides a convenient interface to interact with the 'playlists' endpoint of the YouTube Data API.
It allows users to retrieve information about YouTube playlists by their IDs or get playlists of a specific channel.

Classes:
    Playlists: Encapsulates functions to interact with the 'playlists' endpoint of the YouTube Data API.
"""
from typing import Union

from pytubedata.playlist import Playlist

from pytubedata.config import ENDPOINT_PLAYLIST_PARAM_PART, MAX_RESULTS


class Playlists:
    """
    Encapsulates functions to interact with the `playlists` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_playlist_details(playlist_ids: Union[str, list]) -> Union[PlaylistData, list[PlaylistData]]:
            Get details for a specific YouTube playlist by its ID or fetch multiple playlists at once.

        get_playlists_by_channel(channel_id: str, max_results: int = MAX_RESULTS) -> list:
            Get playlists of a specific channel.

    Raises:
        ValueError: If the playlist_id(s) are invalid or missing.
    """
    ENDPOINT = 'playlists'

    def __init__(self, api_request: object):
        """
        Initializes the Playlist object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.
        """
        self.api_request = api_request

    def get_playlist_details(self, playlist_ids: Union[str, list]) -> Union[Playlist, list[Playlist]]:
        """
        Get details for a specific YouTube playlist by its ID or fetch multiple playlists at once.

        Args:
            playlist_ids (Union[str, list]): The ID(s) of the YouTube playlist(s) to fetch.
                                            Can be a single ID or a list of IDs.

        Returns:
            Union[Playlist, list[PlaylistData]]: A single PlaylistData object if a single playlist is fetched,
                                                    or a list of PlaylistData objects if multiple playlists are fetched.

        Raises:
            ValueError: If the playlist with the provided ID(s) is not found.
        """
        params = {
            "part": ENDPOINT_PLAYLIST_PARAM_PART,
            "id": playlist_ids,
        }

        response: dict = self.api_request.make_request(Playlists.ENDPOINT, params=params)

        if 'items' in response:
            if len(response['items']) > 1:
                return [Playlist(item) for item in response['items']]
            else:
                return Playlist(response['items'][0])
        else:
            raise ValueError(f'Playlist with ID {playlist_ids} not found.')

    def get_playlists_by_channel(self, channel_id: str, max_results: int = MAX_RESULTS) -> list:
        """
        Get playlists of a channel given its id.

        Args:
            channel_id (str): The id of the YouTube channel which playlists to fetch.
            max_results (int): max number of results to fetch in request

        Returns:
            list: The list of PlaylistData object containing the details of the fetched playlists.

        TODO: handle case where channel does not have any playlists
        """
        params = {
            "part": ENDPOINT_PLAYLIST_PARAM_PART,
            "channelId": channel_id,
            "maxResults": max_results,
        }

        response: dict = self.api_request.make_request(Playlists.ENDPOINT, params=params)

        return [Playlist(item) for item in response["items"]]

    # Add other methods for different parameters as needed.
