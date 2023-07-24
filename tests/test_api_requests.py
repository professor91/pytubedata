import unittest
from pytubedata.api_requests import APIRequest

from pytubedata.exceptions import UnauthorizedException


class TestAPIRequest(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.api_request = APIRequest(self.api_key, max_results=20)
        self.api_request_wrong_key = APIRequest('fake_key')

    def test_successful_request(self):
        # Test a successful API request
        response = self.api_request.make_request(
            "videos",
            params={
                "part": "snippet", "id": "N-R5mT-nIDk",
                'key': self.api_key
            }
        )
        self.assertIsInstance(response, dict)

    def test_unauthorized_api_key(self):
        with self.assertRaises(UnauthorizedException):
            self.api_request_wrong_key.make_request(
                "videos",
                params={
                    "part": "snippet", "id": "N-R5mT-nIDk",
                }
            )

    def test_api_failure(self):
        with self.assertRaises(Exception):
            self.api_request.make_request("nonexistent_endpoint")

    def test_handle_pagination(self):
        response = self.api_request._handle_pagination(
            url=self.api_request.BASE_URL+'videos',
            params={
                'part': 'snippet',
                'chart': 'mostPopular',
                'regionCode': 'IN',
                'key': self.api_key,
            }
        )
        self.assertIsInstance(response, list)
        for item in response:
            self.assertIsInstance(item, dict)


if __name__ == "__main__":
    unittest.main()
