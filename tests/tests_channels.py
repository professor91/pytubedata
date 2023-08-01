import unittest
from pytubedata.api_requests import APIRequest
from pytubedata.channels import Channels
from pytubedata.data_models import ChannelData


class TestChannelClass(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.api_request = APIRequest(self.api_key)
        self.channels = Channels(self.api_request)

    def test_get_channel_by_id(self):
        # Replace "your_test_video_id" with a valid YouTube video ID for testing.
        channel_id = "UCsDTy8jvHcwMvSZf_JGi-FA"

        channel_data = self.channels.get_channel_by_id(channel_id)
        self.assertIsInstance(channel_data, ChannelData)
        self.assertEqual(channel_data.id, channel_id)

    # def test_get_channel_by_username(self):
    #     # [TEST-FAIL] TODO: lookup username parameter
    #     username = 'Abhi and Niyu'
    #
    #     channel_data = self.channels.get_channel_by_username(username=username)
    #     self.assertIsInstance(channel_data, ChannelData)


if __name__ == "__main__":
    unittest.main()
