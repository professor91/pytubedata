"""
pytubedata.videos

This module provides a convenient interface to interact with the 'videos' endpoint of the YouTube Data API.
It allows users to retrieve information about YouTube videos by their ids, get popular videos from a region,
get authenticated user's liked or disliked videos.

Classes:
    Videos: Encapsulates functions to interact with the 'videos' endpoint of the YouTube Data API.
"""
from typing import Union

from pytubedata.video import Video

from pytubedata.config import ENDPOINT_VIDEO_PARAM_PART, MAX_RESULTS


class Videos:
    """
    Encapsulates functions to interact with the `videos` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_video_details(video_ids: Union[str, list]) -> Union[VideoData, list[VideoData]]:
            Get details for a specific YouTube video by its ID or fetch multiple playlists at once.

        get_popular_videos(region_code: str = "IN", max_results: int = MAX_RESULTS) -> list:
            Get a list of popular videos in the given region.

        get_my_liked_videos(self, rating: str) -> list:
            Get the list of videos liked/disliked by the authenticated user.

    Raises:
        ValueError: If the video_id(s) are invalid or missing.
    """
    ENDPOINT = 'videos'

    def __init__(self, api_request: object):
        """
        Initializes the Videos object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.
        """
        self.api_request = api_request

    def get_video_details(self, video_ids: Union[str, list]) -> Union[Video, list[Video]]:
        """
        Get details for a specific YouTube video by its ID or fetch multiple videos at once.

        Args:
            video_ids (Union[str, list]): The ID(s) of the YouTube video(s) to fetch.
                                            Can be a single ID or a list of IDs.

        Returns:
            Union[Video, list[VideoData]]: A single VideoData object if a single video is fetched,
                                                    or a list of VideoData objects if multiple videos are fetched.

        Raises:
            ValueError: If the video with the provided ID(s) is not found.
        """
        if isinstance(video_ids, list):
            video_ids: str = ','.join(video_ids)

        params = {
            "part": ENDPOINT_VIDEO_PARAM_PART,
            "id": video_ids,
        }

        response: dict = self.api_request.make_request(Videos.ENDPOINT, params=params)

        if "items" in response:
            if len(response["items"]) > 1:
                return [Video(items) for items in response['items']]
            else:
                return Video(response['items'][0])
        else:
            raise ValueError(f"Video with ID '{video_ids}' not found.")

    def get_popular_videos(self, region_code: str = "IN", max_results: int = MAX_RESULTS) -> list:
        """
        Get a list of popular videos in the given region.

        Args:
            region_code (str, optional): The id of the YouTube channel which playlists to fetch. Defaults to IN.
            max_results (int, optional): max number of results to fetch in request (defaults to MAX_RESULTS from config).

        Returns:
            list: The list of VideoData object containing the details of the fetched videos.

        Raises:
            ValueError: If the popular videos in the provided region_code is not found.
        """
        params = {
            "part": ENDPOINT_VIDEO_PARAM_PART,
            "chart": 'mostPopular',
            "regionCode": region_code,
            "maxResults": max_results,
        }

        response: dict = self.api_request.make_request(Videos.ENDPOINT, params=params)

        if 'items' in response:
            return [Video(item) for item in response["items"]]
        else:
            raise ValueError(f'Popular videos from region {region_code} not found.')

    def get_rated_videos(self, rating: str) -> list:
        """
        Get the list of videos liked/disliked by the authenticated user.

        Args:
            rating (str): Takes only two values `liked` or `disliked`

        Returns:
            list: The list of VideoData object containing the details of the fetched videos.

        Raises:
            ValueError: If the liked or disliked videos not found.
        """
        params = {
            "part": ENDPOINT_VIDEO_PARAM_PART,
            "myRating": rating,
        }

        response: dict = self.api_request.make_request(Videos.ENDPOINT, params=params)

        if 'items' in response:
            return [Video(item) for item in response["items"]]
        else:
            raise ValueError(f'No {str.upper(rating)} videos found.')
