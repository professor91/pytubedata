import unittest
from pytubedata.subscriptions import Subscriptions
from pytubedata.data_models import SubscriptionData


class TestSubscriptionClass(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.subscriptions = Subscriptions(self.api_key)

    def test_get_subscription(self):
        subscription_data = self.subscriptions.get_subscriptions()

        self.assertIsInstance(subscription_data, list)
        for item in subscription_data:
            self.assertIsInstance(item, SubscriptionData)


if __name__ == "__main__":
    unittest.main()
