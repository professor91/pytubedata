from typing import Union

from pytubedata.data_models import ChannelData

from pytubedata.config import ENDPOINT_CHANNEL_PARAM_PART

class Channels:
    """
    Represents `channels` endpoint of YouTube Data API
    """
    ENDPOINT = 'channels'

    def __init__(self, api_request: object):
        self.api_request = api_request

    def get_channel_by_id(self, channel_ids: Union[str, list]) -> Union[ChannelData, list[ChannelData]]:
        """
        Get details for a specific YouTube channel by its ID.
        You can fetch multiple YouTube channels at once.
        """
        params = {
            "part": ENDPOINT_CHANNEL_PARAM_PART,
            "id": channel_ids,
        }

        response: dict = self.api_request.make_request(Channels.ENDPOINT, params=params)

        # Parse the API response and create a ChannelData object.
        if "items" in response:
            if len(response['items']) > 1:
                return [ChannelData(items) for items in response['items']]
            else:
                return ChannelData(response['items'][0])
        else:
            raise ValueError(f"Channel with ID '{channel_ids}' not found.")

    def get_channel_by_username(self, username: str) -> ChannelData:
        """
        Get details for a specific YouTube channel by its username.
        """
        params = {
            "part": ENDPOINT_CHANNEL_PARAM_PART,
            "forUsername": username,
        }

        response: dict = self.api_request.make_request(Channels.ENDPOINT, params=params)

        # Parse the API response and create a ChannelData object.
        if "items" in response and len(response["items"]) > 0:
            return ChannelData(response["items"][0])
        else:
            raise ValueError(f"Channel with username '{username}' not found.")

    # Add other methods for different endpoints of the channels API as needed.
