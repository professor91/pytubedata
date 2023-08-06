from pytubedata.data_models.subscription import SubscriptionData


class Subscription(SubscriptionData):
    """
    Represents a YouTube Subscription
    """
    def __init__(self, data):
        super().__init__(data)
