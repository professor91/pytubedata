from typing import Union

from pytubedata.data_models import VideoData

from pytubedata.config import ENDPOINT_VIDEO_PARAM_PART, MAX_RESULTS


class Videos:
    """
    Represents `videos` endpoint of YouTube Data API
    """
    ENDPOINT = 'videos'

    def __init__(self, api_request: object):
        self.api_request = api_request

    def get_video_details(self, video_ids: Union[str, list]) -> Union[VideoData, list[VideoData]]:
        """
        Get details for a specific video by its ID.
        You can fetch multiple YouTube videos at once.
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
                return [VideoData(items) for items in response['items']]
            else:
                return VideoData(response['items'][0])
        else:
            raise ValueError(f"Video with ID '{video_ids}' not found.")

    def get_popular_videos(self, region_code: str = "IN", max_results: int = MAX_RESULTS) -> list:
        """
        Get a list of popular videos in the given region.
        """
        params = {
            "part": ENDPOINT_VIDEO_PARAM_PART,
            "chart": 'mostPopular',
            "regionCode": region_code,
            "maxResults": max_results,
        }

        response: dict = self.api_request.make_request(Videos.ENDPOINT, params=params)

        if 'items' in response:
            return [VideoData(item) for item in response["items"]]
        else:
            raise ValueError(f'Popular videos from region {region_code} not found.')
