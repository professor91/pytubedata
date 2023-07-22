import unittest
from pytubedata.videos import Videos
from pytubedata.data_models import VideoData


class TestVideosClass(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.videos = Videos(self.api_key)

    def test_get_video_details(self):
        # Replace "your_test_video_id" with a valid YouTube video ID for testing.
        video_id = "N-R5mT-nIDk"

        video_data = self.videos.get_video_details(video_id)
        self.assertIsInstance(video_data, VideoData)
        self.assertEqual(video_data.id, video_id)

    def test_get_popular_videos(self):
        max_results = 5  # You can adjust the number of results to fetch for testing.

        popular_videos = self.videos.get_popular_videos(max_results=max_results)
        self.assertIsInstance(popular_videos, list)
        self.assertGreaterEqual(len(popular_videos), 1)
        for video_data in popular_videos:
            self.assertIsInstance(video_data, VideoData)
            # Add more assertions for other attributes you expect to be present in the response.


if __name__ == "__main__":
    unittest.main()
