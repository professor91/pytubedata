"""
pytubedata.pytubedata

This module server as the primary interface for the users/developers to interact with the API.

Classes:
    YouTubeDataAPIWrapper: Serves as the primary interface for users to interact with the YouTube API
"""
from pytubedata.api_requests import APIRequest
from pytubedata.endpoint.channels import Channels
from pytubedata.endpoint.comment_threads import CommentThreads
from pytubedata.endpoint.comments import Comments
from pytubedata.endpoint.playlists import Playlists
from pytubedata.endpoint.subscriptions import Subscriptions
from pytubedata.endpoint.videos import Videos
# Import other endpoint classes as needed.
from typing import Union


class YouTubeDataAPIWrapper:
    """
    Encapsulates functions to interact with different endpoint of YouTube Data API
    and provides a high level interface to user/developer

    Methods:
        get_channel(channel_id: Union[str, list]) -> ChannelData or list[ChannelData]:
            Fetch details for a specific YouTube channel by its ID or multiple channels at once.

        get_comment_thread(self, comment_thread_id: Union[str, list]) -> CommentThread or list[CommentThread]:
            Fetch details of a specific YouTube comment thread by its ID or multiple comment threads at once.

        get_videos_comment_threads(self, video_id: str) -> list[CommentThread]:
            Fetch all comment threads of a specific YouTube video

        get_comments(comment_id: Union[str, list]) -> CommentData or list[CommentData]:
            Fetch details for a specific YouTube comment by its ID or multiple comments at once.

        get_comment_replies(parent_comment_id: str) -> list[CommentData]:
            Fetch replies to a specific YouTube comment by its parent comment ID.

        get_playlist(playlist_id: Union[str, list]) -> PlaylistData or list[PlaylistData]:
            Fetch details for a specific YouTube playlist by its ID or multiple playlists at once.

        get_channel_playlists(channel_id: str, max_results: int = 10) -> list[PlaylistData]:
            Fetch playlists of a YouTube channel by its ID.

        get_subscriptions() -> list[SubscriptionData] (Requires OAuth access token):
            Fetch the list of channels to which the authenticated user is subscribed.

        get_video(video_id: Union[str, list]) -> VideoData or list[VideoData]:
            Fetch details for a specific YouTube video by its ID or multiple videos at once.
    """
    def __init__(self, api_key: str):
        self.api_request = APIRequest(api_key)
        self.channels = Channels(self.api_request)
        self.comment_threads = CommentThreads(self.api_request)
        self.comments = Comments(self.api_request)
        self.playlists = Playlists(self.api_request)
        self.subscriptions = Subscriptions(self.api_request)
        self.videos = Videos(self.api_request)
        # Initialize other endpoint classes if required.

    def get_channel(self, channel_id: Union[str, list]):
        return self.channels.get_channel_by_id(channel_ids=channel_id)

    def get_comment_thread(self, comment_thread_id: Union[str, list]):
        return self.comment_threads.get_comment_thread_by_id(comment_thread_ids=comment_thread_id)

    def get_videos_comment_threads(self, video_id: str):
        return self.comment_threads.get_video_comment_threads(video_id=video_id)

    def get_comments(self, commend_id: Union[str, list]):
        return self.comments.get_comments(comment_ids=commend_id)

    def get_comment_replies(self, parent_comment_id: str):
        return self.comments.get_replies(parent_comment_id=parent_comment_id)

    def get_playlist(self, playlist_id: Union[str, list]):
        return self.playlists.get_playlist_details(playlist_ids=playlist_id)

    def get_channel_playlists(self, channel_id: str):
        return self.playlists.get_playlists_by_channel(channel_id=channel_id)

    def get_subscriptions(self):
        return self.subscriptions.get_subscriptions()

    def get_video(self, video_id: Union[str, list]):
        return self.videos.get_video_details(video_ids=video_id)

    def get_popular_videos(self, region_code: str = "IN"):
        return self.videos.get_popular_videos(region_code=region_code)
    # Define other public functions for different endpoints as needed.
