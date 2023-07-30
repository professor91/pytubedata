"""
pytubedata.config

This module contains config variables to be used throughout the package.
"""

ENDPOINT_VIDEO_PARAM_PART: str = "contentDetails, id, localizations, snippet, statistics, status, topicDetails"
ENDPOINT_PLAYLIST_PARAM_PART: str = "snippet"
ENDPOINT_COMMENT_PARAM_PART: str = "id, snippet"
ENDPOINT_CHANNEL_PARAM_PART: str = "snippet, statistics"
ENDPOINT_SUBSCRIPTION_PARAM_PART: str = "snippet, contentDetails"
MAX_RESULTS: int = 10
