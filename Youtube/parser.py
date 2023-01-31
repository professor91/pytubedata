"""
Parser module to parse api responses and extract relevant data in structured format
"""
import requests


class Parser:
    @classmethod
    def parse_activity_list_response(cls, response: requests.Response) -> list:
        parsed_data: list = []

        for item in response.json()['items']:
            parsed_data.append(cls._parse_activity_response(item))

        return parsed_data

    @staticmethod
    def _parse_activity_response(data: dict) -> dict:
        # Todo; (NotUrgentIMP) study Activity response
        parsed_data: dict = {
            'activity_id': data['id'],
            'activity_type': data['snippet']['type'],
            "content_detail": data['contentDetails'],
            'channel_id': data['snippet']['channelId'],
            'activity_title': data['snippet']['title'],
            'activity_description': data['snippet']['description'],
            'published_at': data['snippet']['publishedAt'],
        }

        return parsed_data

    @staticmethod
    def parse_channel_response(response: requests.Response) -> dict:
        data: dict = response.json()['items'][0]

        parsed_data = {
            'channel_id': data['id'],
            'title': data['snippet']['title'],
            'description': data['snippet']['description'],
            "custom_url": data['snippet']['customUrl'],
            'created_at': data['snippet']['publishedAt'],
            'country': data['snippet']['country'],
            'view_count': data['statistics']['viewCount'],
            'subscriber_count': data['statistics']['subscriberCount'],
            'video_count': data['statistics']['videoCount'],
            'topic_ids': data['topicDetails']['topicIds'],
            'topic_categories': data['topicDetails']['topicCategories'],
            'keywords': data['brandingSettings']['channel']['keywords'],
            'uploads_playlist_id': data['contentDetails']['relatedPlaylists']['uploads'],
            'thumbnail': data['snippet']['thumbnails']['default']['url'],
            'bannerExternalUrl': data['brandingSettings']['image']['bannerExternalUrl']
        }

        return parsed_data

    @classmethod
    def parse_channel_section_list_response(cls, response: requests.Response) -> list:
        parsed_data: list = []

        for item in response.json()['items']:
            parsed_data.append(cls._parse_channel_section_response(item))

        return parsed_data

    @staticmethod
    def _parse_channel_section_response(data: dict) -> dict:
        parsed_data: dict = {
            'section_id': data['id'],
            'section_type': data['snippet']['type'],
            'channel_id': data['snippet']['channelId']
        }

        return parsed_data

    @classmethod
    def parse_playlist_list_response(cls, response: requests.Response) -> list:
        parsed_data: list = []

        for item in response.json()['items']:
            parsed_data.append(cls._parse_playlist_response(item))

        return parsed_data

    @staticmethod
    def _parse_playlist_response(data: dict) -> dict:
        parsed_data: dict = {
            'playlist_id': data['id'],
            'channel_id': data['snippet']['channelId'],
            'title': data['snippet']['title'],
            'description': data['snippet']['description'],
            'video_count': data['contentDetails']['itemCount'],
            'thumbnail': data['snippet']['thumbnails']['default']['url'],
        }

        return parsed_data

    @classmethod
    def parse_playlist_video_list_response(cls, response: requests.Response) -> list:
        parsed_data: list = []

        for item in response.json()['items']:
            parsed_data.append(cls._parse_playlist_video_response(item))

        return parsed_data

    @staticmethod
    def _parse_playlist_video_response(data: dict) -> dict:
        parsed_data: dict = {
            'video_id': data['contentDetails']['videoId'],
            'playlist_id': data['snippet']['playlistId'],
            'channel_id': data['snippet']['channelId'],
            'video_title': data['snippet']['title'],
            'video_description': data['snippet']['description'],
            'published_at': data['contentDetails']['videoPublishedAt'],
            'thumbnail': data['snippet']['thumbnails']['default']['url'],
        }

        return parsed_data

    @staticmethod
    def parse_video_response(response: requests.Response) -> dict:
        data: dict = response.json()['items'][0]

        return {
            'video_id': [data['id']],
            'channel_id': [data['snippet']['channelId']],
            'title': [data['snippet']['title']],
            'description': [data['snippet']['title']],
            'published_at': [data['snippet']['publishedAt']],
            'views_count': [data['statistics']['viewCount']],
            'likes_count': [data['statistics']['likeCount']],
            'comment_count': [data['statistics']['commentCount']],
            'duration': [data['contentDetails']['duration']],
            'tage': [data['snippet']['tags']],
            'category': [data['snippet']['categoryId']],
            'topics': [data['topicDetails']['topicCategories']],
            'dimension': [data['contentDetails']['dimension']],
            'definition': [data['contentDetails']['definition']],
            'caption': [data['contentDetails']['caption']],
            'blocked_region': [data['contentDetails']['regionRestriction']],
            'license': [data['status']['license']],
            'default_audio_lang': [data['snippet']['defaultAudioLanguage']],
            'embeddable': [data['status']['embeddable']]
        }

    @classmethod
    def parse_comments_list_response(cls, response: requests.Response) -> list:
        parsed_data: list = []

        for item in response.json()['items']:
            parsed_data.append(cls._parse_comment_response(item))

        return parsed_data

    @staticmethod
    def _parse_comment_response(data: dict) -> dict:
        parsed_data: dict = {
            'comment_id': data['id']
        }

        return parsed_data

    @staticmethod
    def parse_comment_responses(response: requests.Response) -> dict:
        data: dict = response.json()['items'][0]
        parsed_data: dict = {
            'comment_id': data['id'],
            'text_original': data['snippet']['textOriginal'],
            'author_name': data['snippet']['authorDisplayName'],
            'author_channel_id': data['snippet']['authorChannelId'],
            'author_channel_url': data['snippet']['authorChannelUrl'],
            'published_at': data['snippet']['publishedAt'],
            'updated_at': data['snippet']['updatedAt'],
            'likes_count': data['snippet']['likeCount'],
            'viewer_rating': data['snippet']['viewerRating']

        }

        return parsed_data
