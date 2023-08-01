"""
pytubedata.data_models

This module contains data model classes to represent different API endpoint responses from the YouTube Data API.

Classes:
    VideoData: Represents the API response for the 'videos' endpoint.
    ChannelData: Represents the API response for the 'channels' endpoint.
    PlaylistData: Represents the API response for the 'playlists' endpoint.
    CommentData: Represents the API response for the 'comments' endpoint.
    SubscriptionData: Represents the API response for the 'subscriptions' endpoint.
"""


class VideoData:
    """
    Represents the API response for the 'videos' endpoint.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["snippet"]["title"]
        self.description = data["snippet"]["description"]
        self.published_at = data["snippet"]["publishedAt"]
        self.channel_id = data['snippet']['channelId']
        self.channel_title = data["snippet"]["channelTitle"]
        self.category_id = data['snippet']['categoryId']
        self.duration = data['contentDetails']['duration']
        self.views = data["statistics"]["viewCount"]
        self.likes = data['statistics']['likeCount']
        self.favourite_count = data['statistics']['favoriteCount']
        self.comment_count = data['statistics']['commentCount']
        self.topic_categories = data['topicDetails']['topicCategories']
        # Add more attributes as needed.


class ChannelData:
    """
    Represents the API response for the 'channels' endpoint.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["snippet"]["title"]
        self.description = data["snippet"]["description"]
        self.published_at = data["snippet"]["publishedAt"]
        self.country = data["snippet"]["country"]
        self.custom_url = data["snippet"].get("customUrl", None)
        # Add more attributes as needed.


class PlaylistData:
    """
    Represents the API response for the 'playlists' endpoint.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["snippet"]["title"]
        self.description = data["snippet"]["description"]
        self.published_at = data["snippet"]["publishedAt"]
        self.channel_id = data["snippet"]["channelId"]
        self.channel_title = data["snippet"]["channelTitle"]
        self.thumbnail_url = data["snippet"]["thumbnails"]["default"]["url"]
        # Add more attributes as needed.


class CommentData:
    """
    Represents the API response for the 'comments' endpoint.
    """
    def __init__(self, data):
        self.id = data["id"]
        self.author_name = data["snippet"]["authorDisplayName"]
        self.author_profile_image_url = data['snippet']['authorProfileImageUrl']
        self.author_channel_url = data['snippet']['authorChannelUrl']
        self.author_channel_id = data["snippet"]["authorChannelId"]["value"]
        self.text = data["snippet"]["textDisplay"]
        self.text_og = data['snippet']['textOriginal']
        self.published_at = data["snippet"]["publishedAt"]
        self.updated_at = data['snippet']['updatedAt']
        self.can_rate = data['snippet']['canRate']
        self.likes = data['snippet']['likeCount']


class CommentThreadData:
    """
    Represents the API response for the 'commentThreads' endpoint.
    """
    def __init__(self, data):
        self.id: str = data["id"]
        self.top_level_comment: object = CommentData(data["snippet"]["topLevelComment"])
        self.can_reply: bool = data["snippet"]["canReply"]
        self.reply_count: int = data["snippet"]["totalReplyCount"]
        if self.reply_count > 0:
            self.replies: list[CommentData] = [CommentData(item) for item in data["replies"]["comments"]]


class SubscriptionData:
    """
    Represents the API response for the 'subscriptions' endpoint.
    """
    def __init__(self, data):
        self.id = data.get("id")
        self.channel_id = data['snippet']['channelId']
        self.channel_name = data['snippet']['title']
        self.channel_description = data['snippet']['description']
        self.subscribed_on = data['snippet']['publishedAt']
        self.video_count = data['contentDetails']['totalItemCount']
