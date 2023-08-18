"""
pytubedata.comments

This module provides a convenient interface to interact with the 'comment' endpoint of the YouTube Data API.
It allows users to retrieve information about YouTube comments by their IDs or get replies to a specific comment.

Classes:
    Comments: Encapsulates functions to interact with the 'comments' endpoint of the YouTube Data API.
"""
from typing import Union

from pytubedata.comment import Comment

from pytubedata.config import ENDPOINT_COMMENT_PARAM_PART


class Comments:
    """
    Encapsulates functions to interact with the `comments` endpoint of YouTube Data API

    Attributes:
        ENDPOINT (str): The endpoint name of YouTube data api.

    Methods:
        get_comments(comment_ids: Union[str, list], **kwargs) -> Union[CommentData, list[CommentData]]:
            Get details for a specific YouTube comment by its ID or fetch multiple comments at once.

        get_replies(parent_comment_id: str, **kwargs) -> list:
            Get replies to a comment.

    Raises:
        ValueError: If the comment_id(s) are invalid or missing.
    """
    ENDPOINT = 'comments'

    def __init__(self, api_request: object):
        """
        Initializes the Comment object with the provided APIRequest instance.

        Args:
            api_request (object): An instance of APIRequest used to make requests to the YouTube Data API.
        """
        self.api_request = api_request

    def get_comments(self, comment_ids: Union[str, list], **kwargs) -> Union[Comment, list[Comment]]:
        """
        Get details for a specific YouTube comment by its ID or fetch multiple comments at once.

        Args:
            comment_ids (Union[str, list]): The ID(s) of the YouTube comments(s) to fetch.
                                            Can be a single ID or a list of IDs.

            kwargs: Check the official documentation for additional parameter to customize the request

        Returns:
            Union[Comment, list[CommentData]]: A single CommentData object if a single channel is fetched,
                                                    or a list of CommentData objects if multiple comments are fetched.

        Raises:
            ValueError: If the comment with the provided ID(s) is not found.
        """
        if isinstance(comment_ids, list):
            comment_ids = ','.join(comment_ids)

        params = {
            'part': ENDPOINT_COMMENT_PARAM_PART,
            'id': comment_ids,
        }
        params.update(kwargs)

        response: dict = self.api_request.make_request(Comments.ENDPOINT, params=params)

        if "items" in response:
            if len(response["items"]) > 1:
                return [Comment(item) for item in response['items']]
            else:
                return Comment(response['items'][0])
        else:
            raise ValueError(f"Comment with ID '{comment_ids}' not found.")

    def get_replies(self, parent_comment_id: str, **kwargs) -> list:
        """
        Get replies to a comment given its id.

        Args:
            parent_comment_id (str): The id of the YouTube comment which replies to fetch.

            kwargs: Check the official documentation for additional parameter to customize the request

        Returns:
            list: The list of  CommentData object containing the details of the fetched replies (comments).

        Raises:
            ValueError: If the comment with the provided id is not found.
        """
        params = {
            'part': 'id, snippet',
            'parentId': parent_comment_id,
        }
        params.update(kwargs)

        response: dict = self.api_request.make_request(Comments.ENDPOINT, params=params)

        if 'items' in response:
            return [Comment(item) for item in response['items']]
        else:
            raise ValueError(f"Comment with ID '{parent_comment_id}' has no replies.")
