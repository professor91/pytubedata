import unittest
from pytubedata.api_requests import APIRequest
from pytubedata.comment_threads import CommentThreads


class TestCommentThreadClass(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.api_request = APIRequest(self.api_key)
        self.comment_thread = CommentThreads(self.api_request)


if __name__ == "__main__":
    unittest.main()
