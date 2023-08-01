"""
pytubedata.config

This module contains config variables to be used throughout the package.
"""

ENDPOINT_CHANNEL_PARAM_PART: str = "snippet, contentDetails, statistics"
ENDPOINT_COMMENT_THREAD_PARAM_PART: str = "snippet, replies"
ENDPOINT_COMMENT_PARAM_PART: str = "id, snippet"
ENDPOINT_PLAYLIST_PARAM_PART: str = "snippet"
ENDPOINT_SUBSCRIPTION_PARAM_PART: str = "snippet, contentDetails"
ENDPOINT_VIDEO_PARAM_PART: str = "contentDetails, id, localizations, snippet, statistics, status, topicDetails"
MAX_RESULTS: int = 10
