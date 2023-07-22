# todo: go through video, channel, playlist etc resources and add all the necessary attributes in the respective model

class VideoData:
    """
    Represents the APIs Video endpoint responses
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
    Represents the APIs Channel endpoint responses
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
    Represents the APIs Playlist endpoint responses
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
    Represents the APIs Comment endpoint responses
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

