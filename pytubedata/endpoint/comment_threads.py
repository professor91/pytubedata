"""
pytubedata.comment_threads

This module provides a convenient interface to interact with the 'commentThreads' endpoint of the YouTube Data API.
It allows users to retrieve comment threads from YouTube videos or channels.

Classes:
    CommentThreads: Encapsulates functions to interact with the 'commentThreads' endpoint of the YouTube Data API.
"""
from typing import Union

from pytubedata.comment_thread import CommentThread

from pytubedata.config import ENDPOINT_COMMENT_THREAD_PARAM_PART


class CommentThreads:
    """
    Encapsulates functions to interact with the `commentThreads` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_video_comment_threads(video_id: str) -> list[CommentThreadData]:
            Get all comments from a specific YouTube video by its ID.

        get_channel_comment_threads(channel_id: str) -> list[CommentThreadData]:
            Get all comments for a specific YouTube channel by its ID.

    Raises:
        ValueError: If the comment_id(s) are invalid or missing.
    """
    ENDPOINT = 'commentThreads'

    def __init__(self, api_request: object):
        """
        Initializes the Comment object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.
        """
        self.api_request = api_request

    def get_comment_thread_by_id(self, comment_thread_ids: Union[str, list]) -> Union[CommentThread, list[CommentThread]]:
        """
        Get details for a specific YouTube comment by its ID or fetch multiple comments at once.

        Args:
            comment_thread_ids (Union[str, list]): The ID(s) of the YouTube comments thread(s) to fetch.
                                                    Can be a single ID or a list of IDs.

        Returns:
            Union[CommentThread, list[CommentThreadData]]: A single CommentThreadData object if a single comment thread is fetched,
                                                                or a list of CommentThreadData objects if multiple comment threads are fetched.

        Raises:
            ValueError: If the comment thread with the provided ID(s) is not found.
        """
        params = {
            'part': ENDPOINT_COMMENT_THREAD_PARAM_PART,
            'id': comment_thread_ids
        }

        response: dict = self.api_request.make_request(CommentThreads.ENDPOINT, params=params)

        if "items" in response:
            if len(response["items"]) > 1:
                return [CommentThread(item) for item in response['items']]
            else:
                return CommentThread(response['items'][0])
        else:
            raise ValueError(f"Comment Thread with ID '{comment_thread_ids}' not found.")

    def get_video_comment_threads(self, video_id: str) -> list[CommentThread]:
        """
        Get all comments from a specific YouTube video by its ID.

        Args:
            video_id (str): The ID of the YouTube video for which comments to be fetched.

        Returns:
            list[CommentThread]: A list of CommentThreadData objects.

        Raises:
            ValueError: If the comment thread with the provided video id is not found.
        """
        params = {
            'part': ENDPOINT_COMMENT_THREAD_PARAM_PART,
            'videoId': video_id,
        }

        response: dict = self.api_request.make_request(CommentThreads.ENDPOINT, params=params)

        if len(response["items"]) > 0:
            return [CommentThread(item) for item in response['items']]
        else:
            raise ValueError(f"Comment Thread for video with ID '{video_id}' not found.")

    # def get_channel_comment_threads(self, channel_id: str) -> list[CommentThreadData]:
    #     """
    #     Get all comments for a specific YouTube channel by its ID. Does not include comments on videos uploaded by
    #     channel.
    #
    #     Args:
    #         channel_id (str): The ID of the YouTube channel for which comments to be fetched.
    #
    #     Returns:
    #         list[CommentThreadsData]: A list of CommentThreadsData object
    #     Raises:
    #         ValueError: If the comment thread with the provided channel id is not found.
    #     """
    #     params = {
    #         'part': ENDPOINT_COMMENT_THREAD_PARAM_PART,
    #         'channelId': channel_id,
    #     }
    #
    #     response: dict = self.api_request.make_request(CommentThreads.ENDPOINT, params=params)
    #
    #     if len(response["items"]) > 0:
    #         return [CommentThreadData(item) for item in response['items']]
    #     else:
    #         raise ValueError(f"Comment Thread for channel with ID '{channel_id}' not found.")
