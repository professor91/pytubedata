from typing import Union

from pytubedata.api_requests import APIRequest
from pytubedata.data_models import VideoData


class Videos:
    """
    Represents `videos` endpoint of YouTube Data API
    """
    ENDPOINT = 'videos'

    def __init__(self, api_key: str,):
        self.api_request = APIRequest(api_key)

    def get_video_details(self, video_ids: Union[str, list]) -> Union[VideoData, list[VideoData]]:
        """
        Get details for a specific video by its ID.
        You can fetch multiple YouTube videos at once.
        """
        if isinstance(video_ids, list):
            video_ids: str = ','.join(video_ids)

        params = {
            "part": "contentDetails, id, localizations, snippet, statistics, status, topicDetails",
            "id": video_ids,
        }

        response: dict = self.api_request.make_request(Videos.ENDPOINT, params=params)

        if "items" in response:
            if len(response["items"]) > 1:
                return [VideoData(items) for items in response['items']]
            else:
                return VideoData(response['items'][0])
        else:
            raise ValueError(f"Video with ID '{video_ids}' not found.")

    def get_popular_videos(self, region_code: str = "IN", max_results: int = 10) -> list:
        """
        Get a list of popular videos in the given region.
        """
        params = {
            "part": "contentDetails, id, localizations, snippet, statistics, status, topicDetails",
            "chart": 'mostPopular',
            "regionCode": region_code,
            "maxResults": max_results,
        }

        response: dict = self.api_request.make_request(Videos.ENDPOINT, params=params)

        if 'items' in response:
            return [VideoData(item) for item in response["items"]]
        else:
            raise ValueError(f'Popular videos from region {region_code} not found.')
