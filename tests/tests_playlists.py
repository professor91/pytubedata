import unittest
from pytubedata.playlists import Playlists
from pytubedata.data_models import PlaylistData


class TestPlaylistsClass(unittest.TestCase):
    def setUp(self):
        with open('secret.yml', 'r') as rf:
            self.api_key = rf.read()
        self.playlists = Playlists(self.api_key)

    def test_get_playlist_details(self):
        # Replace "your_test_playlist_id" with a valid YouTube playlist ID for testing.
        playlist_id = "PLGwmAEmjn4fk0-8ZwSpHlayweS0xf_jLS"

        playlist_data = self.playlists.get_playlist_details(playlist_id)
        self.assertIsInstance(playlist_data, PlaylistData)
        self.assertEqual(playlist_data.id, playlist_id)

    def test_get_playlists_by_channel(self):
        # Replace "your_test_channel_id" with a valid YouTube channel ID for testing.
        channel_id = "UCsDTy8jvHcwMvSZf_JGi-FA"
        max_results = 5  # You can adjust the number of results to fetch for testing.

        channel_playlists = self.playlists.get_playlists_by_channel(
            channel_id, max_results=max_results
        )
        self.assertIsInstance(channel_playlists, list)
        self.assertGreaterEqual(len(channel_playlists), 1)
        for playlist_data in channel_playlists:
            self.assertIsInstance(playlist_data, PlaylistData)


if __name__ == "__main__":
    unittest.main()
