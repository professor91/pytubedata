from typing import Union

from pytubedata.data_models import SubscriptionData

from pytubedata.config import ENDPOINT_SUBSCRIPTION_PARAM_PART


class Subscriptions:
    """
    Represents `subscriptions` endpoint of YouTube Data API
    """
    ENDPOINT = 'subscriptions'

    def __init__(self, api_request: object):
        self.api_request = api_request

    def get_subscriptions(self) -> Union[SubscriptionData, list[SubscriptionData]]:
        """
        Get the user's subscriptions
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
