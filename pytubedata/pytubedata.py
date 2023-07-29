from pytubedata.api_requests import APIRequest
from pytubedata.videos import Videos
from pytubedata.channels import Channels
from pytubedata.playlists import Playlists
from pytubedata.comments import Comment
from pytubedata.subscriptions import Subscriptions
# Import other endpoint classes as needed.


class YouTubeDataAPIWrapper:
    """
    Serves as the primary interface for users to interact with the API
    """
    def __init__(self, api_key: str):
        self.api_request = APIRequest(api_key)
        self.videos = Videos(self.api_request)
        self.channels = Channels(self.api_request)
        self.playlists = Playlists(self.api_request)
        self.comments = Comment(self.api_request)
        self.subscriptions = Subscriptions(self.api_request)
        # Initialize other endpoint classes if required.

    def get_channel(self, channel_id: str):
        return self.channels.get_channel_by_id(channel_id)

    def get_video(self, video_id: str):
        return self.videos.get_video_details(video_id)

    def get_playlist(self, playlist_id: str):
        return self.playlists.get_playlist_details(playlist_ids=playlist_id)

    def get_channel_playlists(self, channel_id: str, max_results: int = 10):
        return self.playlists.get_playlists_by_channel(channel_id=channel_id, max_results=max_results)

    def get_comments(self, commend_id: str):
        return self.comments.get_comments(comment_ids=commend_id)

    def get_comment_replies(self, parent_comment_id: str):
        return self.comments.get_replies(parent_comment_id=parent_comment_id)

    def get_subscriptions(self):
        return self.subscriptions.get_subscriptions()
    # Define other public functions for different endpoints as needed.
