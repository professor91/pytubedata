"""
pytubedata.data_models.comment_thread

This module contains data model class for `commentThreads` endpoint of YouTube Data API

Classes:
    CommentThreadData: Represents the API response for the 'commentThreads' endpoint.
"""
from typing import Union

from pytubedata.data_models.comment import CommentData


class CommentThreadData:
    """
    Represents the API response for the 'commentThreads' endpoint.
    """
    def __init__(self, data):
        self._data = data

    @property
    def id(self) -> str:
        return self._data['id']

    @property
    def top_level_comment(self) -> CommentData:
        return CommentData(self._data['snippet']['topLevelComment'])

    @property
    def can_reply(self) -> bool:
        return self._data['snippet']['canReply']

    @property
    def reply_count(self) -> int:
        return self._data['snippet']['totalReplyCount']

    @property
    def replies(self) -> Union[list[CommentData], None]:
        if self.reply_count > 0:
            return [CommentData(item) for item in self._data['replies']['comments']]
        else:
            return None
