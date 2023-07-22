from typing import Union

from pytubedata.api_requests import APIRequest
from pytubedata.data_models import PlaylistData


class Playlists:
    """
    Represents `playlists` endpoint of YouTube Data API
    """
    ENDPOINT = 'playlists'

    def __init__(self, api_key: str):
        self.api_request = APIRequest(api_key)

    def get_playlist_details(self, playlist_ids: Union[str, list]) -> Union[PlaylistData, list[PlaylistData]]:
        """
        Get details for a specific playlist by its ID.
        You can fetch multiple YouTube playlists at once.
        """
        params = {
            "part": "snippet",
            "id": playlist_ids,
        }

        response: dict = self.api_request.make_request(Playlists.ENDPOINT, params=params)

        if 'items' in response:
            if len(response['items']) > 1:
                return [PlaylistData(item) for item in response['items']]
            else:
                return PlaylistData(response['items'][0])
        else:
            raise ValueError(f'Playlist with ID {playlist_ids} not found.')

    def get_playlists_by_channel(self, channel_id: str, max_results: int = 10) -> list:
        """
        Get playlists of a specific channel.
        """
        params = {
            "part": "snippet",
            "channelId": channel_id,
            "maxResults": max_results,
        }

        response: dict = self.api_request.make_request(Playlists.ENDPOINT, params=params)

        return [PlaylistData(item) for item in response["items"]]

    # Add other methods for different parameters as needed.
