"""
pytubedata.

This module provides a convenient interface to interact with the 'subscriptions' endpoint of the YouTube Data API.
It allows users to get list of their subscriptions.

Classes:
    Subscriptions: Encapsulates functions to interact with the 'subscriptions' endpoint of the YouTube Data API.
"""
from typing import Union

from pytubedata.data_models import SubscriptionData

from pytubedata.config import ENDPOINT_SUBSCRIPTION_PARAM_PART


class Subscriptions:
    """
    Encapsulates functions to interact with the `subscriptions` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_subscriptions() -> Union[SubscriptionData, list[SubscriptionData]]:
            Get the user's subscriptions

    Raises:
        ValueError: If user do not have any subscriptions.
    """
    ENDPOINT = 'subscriptions'

    def __init__(self, api_request: object):
        """
        Initializes the Playlist object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.

        Note: APIRequest object must have access_token since this class makes authorized requests
        """
        self.api_request = api_request

    def get_subscriptions(self) -> Union[SubscriptionData, list[SubscriptionData]]:
        """
        Get the user's subscriptions

        Returns:
            Union[SubscriptionData, list[SubscriptionData]]: A single SubscriptionData object if a single subscriber is found,
                                                    or a list of SubscriptionData objects if multiple subscription are found.

        Raises:
            ValueError: If user do not have any subscription.
        """
        params = {
            'part': ENDPOINT_SUBSCRIPTION_PARAM_PART,
            'mine': True,
        }

        response: dict = self.api_request.make_request(Subscriptions.ENDPOINT, params=params, authorize=True)

        if 'items' in response:
            if len(response['items']) > 1:
                return [SubscriptionData(item) for item in response['items']]
            else:
                return SubscriptionData(response['items'][0])
        else:
            raise ValueError('Subscribers for user not found.')
