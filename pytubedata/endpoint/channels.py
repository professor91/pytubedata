"""
pytubedata.channels

This module provides a convenient interface to interact with the 'channels' endpoint of the YouTube Data API.
It allows users to retrieve information about YouTube channels by their IDs or usernames.

Classes:
    Channels: Encapsulates functions to interact with the 'channels' endpoint of the YouTube Data API.
"""
from typing import Union

from pytubedata.channel import Channel

from pytubedata.config import ENDPOINT_CHANNEL_PARAM_PART


class Channels:
    """
    Encapsulates functions to interact with the `channels` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_channel_by_id(channel_ids: Union[str, list]) -> Union[ChannelData, list[ChannelData]]:
            Get details for a specific YouTube channel by its ID or fetch multiple channels at once.

        get_channel_by_username(username: str) -> ChannelData:
            Get details for a specific YouTube channel by its username.

    Raises:
        ValueError: If the channel_id or channel username are invalid or missing.
    """
    ENDPOINT = 'channels'

    def __init__(self, api_request: object):
        """
        Initializes the Channels object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.
        """
        self.api_request = api_request

    def get_channel_by_id(self, channel_ids: Union[str, list]) -> Union[Channel, list[Channel]]:
        """
        Get details for a specific YouTube channel by its ID or fetch multiple channels at once.

        Args:
            channel_ids (Union[str, list]): The ID(s) of the YouTube channel(s) to fetch.
                                            Can be a single ID or a list of IDs.

        Returns:
            Union[Channel, list[ChannelData]]: A single ChannelData object if a single channel is fetched,
                                                    or a list of ChannelData objects if multiple channels are fetched.

        Raises:
            ValueError: If the channel with the provided ID(s) is not found.
        """
        params = {
            "part": ENDPOINT_CHANNEL_PARAM_PART,
            "id": channel_ids,
        }

        response: dict = self.api_request.make_request(Channels.ENDPOINT, params=params)

        # Parse the API response and create a ChannelData object.
        if "items" in response:
            if len(response['items']) > 1:
                return [Channel(items) for items in response['items']]
            else:
                return Channel(response['items'][0])
        else:
            raise ValueError(f"Channel with ID '{channel_ids}' not found.")

    # def get_channel_by_username(self, username: str) -> ChannelData:
    #     """
    #     Get details for a specific YouTube channel by its username.
    #
    #     Args:
    #         username (str): The username of the YouTube channel to fetch.
    #
    #     Returns:
    #         ChannelData: The ChannelData object containing the details of the fetched channel.
    #
    #     Raises:
    #         ValueError: If the channel with the provided username is not found.
    #     """
    #     params = {
    #         "part": ENDPOINT_CHANNEL_PARAM_PART,
    #         "forUsername": username,
    #     }
    #
    #     response: dict = self.api_request.make_request(Channels.ENDPOINT, params=params)
    #
    #     # Parse the API response and create a ChannelData object.
    #     if "items" in response and len(response["items"]) > 0:
    #         return ChannelData(response["items"][0])
    #     else:
    #         raise ValueError(f"Channel with username '{username}' not found.")

    # Add other methods for different endpoints of the channels API as needed.
