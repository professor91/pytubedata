from typing import Union

from pytubedata.data_models import CommentData

from pytubedata.config import ENDPOINT_COMMENT_PARAM_PART


class Comment:
    """
    Represents `comments` endpoint of YouTube Data API
    """
    ENDPOINT = 'comments'

    def __init__(self, api_request: object):
        self.api_request = api_request

    def get_comments(self, comment_ids: Union[str, list]) -> Union[CommentData, list[CommentData]]:
        """
        Get details for a specific comment by its ID.
        """
        if isinstance(comment_ids, list):
            comment_ids = ','.join(comment_ids)

        params = {
            'part': ENDPOINT_COMMENT_PARAM_PART,
            'id': comment_ids,
        }

        response: dict = self.api_request.make_request(Comment.ENDPOINT, params=params)

        if "items" in response:
            if len(response["items"]) > 1:
                return [CommentData(item) for item in response['items']]
            else:
                return CommentData(response['items'][0])
        else:
            raise ValueError(f"Comment with ID '{comment_ids}' not found.")

    def get_replies(self, parent_comment_id: str) -> list:
        """
        Get replies of a parent comment
        """
        params = {
            'part': 'id, snippet',
            'parentId': parent_comment_id,
        }

        response: dict = self.api_request.make_request(Comment.ENDPOINT, params=params)

        if 'items' in response:
            return [CommentData(item) for item in response['items']]
        else:
            raise ValueError(f"Comment with ID '{parent_comment_id}' has no replies.")
