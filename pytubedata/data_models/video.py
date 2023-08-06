"""
pytubedata.data_models.video

This module contains data model class for `videos` endpoint of YouTube Data API

Classes:
    VideoData: Represents the API response for the 'videos' endpoint.
"""


class VideoData:
    """
    Represents the API response for the 'videos' endpoint.
    """
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data["id"]
        
    @property
    def title(self) -> str:
        return self._data["snippet"]["title"]
        
    @property
    def description(self) -> str:
        return self._data["snippet"]["description"]
        
    @property
    def published_at(self) -> str:
        return self._data["snippet"]["publishedAt"]
        
    @property
    def channel_id(self) -> str:
        return self._data['snippet']['channelId']
        
    @property
    def channel_title(self) -> str:
        return self._data["snippet"]["channelTitle"]
        
    @property
    def category_id(self) -> str:
        return self._data['snippet']['categoryId']
        
    @property
    def duration(self) -> str:
        return self._data['contentDetails']['duration']
        
    @property
    def views(self) -> int:
        return self._data["statistics"]["viewCount"]
        
    @property
    def likes(self) -> int:
        return self._data['statistics']['likeCount']
        
    @property
    def favourite_count(self) -> int:
        return self._data['statistics']['favoriteCount']
        
    @property
    def comment_count(self) -> int:
        return self._data['statistics']['commentCount']
        
    @property
    def topic_categories(self) -> str:
        return self._data['topicDetails']['topicCategories']
