import unittest
from pytubedata.comments import Comment
from pytubedata.data_models import CommentData


class TestVideosClass(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.comments = Comment(self.api_key)

    def test_get_comments(self):
        comment_ids = 'UgxAkHWgQU2sMVcsQlx4AaABAg'

        comment_data = self.comments.get_comments(comment_ids)
        self.assertIsInstance(comment_data, CommentData)
        self.assertEqual(comment_data.id, comment_ids)

    def test_get_replies(self):
        comment_id = 'UgxAkHWgQU2sMVcsQlx4AaABAg'

        comment_replies = self.comments.get_replies(parent_comment_id=comment_id)
        self.assertIsInstance(comment_replies, list)
        self.assertGreaterEqual(len(comment_replies), 1)
        for comment_data in comment_replies:
            self.assertIsInstance(comment_data, CommentData)


if __name__ == "__main__":
    unittest.main()
