# https://developers.google.com/youtube/v3/docs/commentThreads
# https://developers.google.com/youtube/v3/docs/comments

class Comment:
    """
    The comment class handles the methods to fetch data from the YouTube Data API related to comments
    """
    def __init__(self):
        pass

    def get_for_video(self, **kwargs) -> tuple:
        """
        Given a video `id` returns top level comments on the video.

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        :param id:
            :required:
            desc: The ID of a video i.e. "kNbhUWLH_yY", this can be found at the end of YouTube urls
            :type str:

        :param maxResults:
            :optional:
            desc: maximum items that should be returned in response
            :type unsigned int:

        :param order:
            :optional:
            desc: Specifies the order in which the API response should list comment threads
            :type str choice from [time, relevance]:

        :param searchTerms:
            :optional:
            desc: Instructs the API to limit the API response to only contain comments that contain the specified search terms
            :type str:

        :param textFormat:
            :optional:
            desc: Instruct the API to return the comments left by users in html formatted or in plain text
            :type choice from [html, text]:

        :returns top level comments on the given videos `id`:
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "videoId": kwargs.get('id'),
            "part": "snippet, replies",
        }
        kwargs.pop('id')
        params.update(kwargs)

        return "/commentThreads", params

    # Todo- debug error for get_comment_for_channel
    def get_for_channel(self, **kwargs) -> tuple:
        """
        Given a channel `id` returns comment threads containing comments about the specified channel (excluding comments left on videos that the channel uploaded).

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            :type str:

        :param maxResults:
            :optional:
            desc: maximum items that should be returned in response
            :type unsigned int:

        :param order:
            :optional:
            desc: Specifies the order in which the API response should list comment threads
            :type str choice from [time, relevance]:

        :param searchTerms:
            :optional:
            desc: Instructs the API to limit the API response to only contain comments that contain the specified search terms
            :type str:

        :param textFormat:
            :optional:
            desc: Instruct the API to return the comments left by users in html formatted or in plain text
            :type choice from [html, text]:

        :returns top level comments related to the given channel `id':
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "channelId": kwargs.get('id'),
            "part": "snippet"
        }
        kwargs.pop('id')
        params.update(kwargs)
        
        return "/commentThreads", params

    def get_related_to_channel(self, **kwargs) -> tuple:
        """
        Given a channel `id` returns comment threads associated with the channel(include comments about the channel or about the channel's videos).

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            :type str:

        :param maxResults:
            :optional:
            desc: maximum items that should be returned in response
            :type unsigned int:

        :param order:
            :optional:
            desc: Specifies the order in which the API response should list comment threads
            :type str choice from [time, relevance]:

        :param searchTerms:
            :optional:
            desc: Instructs the API to limit the API response to only contain comments that contain the specified search terms
            :type str:

        :param textFormat:
            :optional:
            desc: Instruct the API to return the comments left by users in html formatted or in plain text
            :type choice from [html, text]:

        :returns top level comments related to the given channel `id':
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "allThreadsRelatedToChannelId": kwargs.get('id'),
            "part": "snippet, replies",
        }
        kwargs.pop('id')
        params.update(kwargs)

        return "/commentThreads", params

    def get_replies(self, **kwargs) -> tuple:
        """
        Given a comment `id`s returns the metadata of that comment with replies.

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        :param id(s):
            :required:
            desc: The ID of a comment i.e. "UgyH6pdCkC_oBCjmm9Z4AaABAg.9hAFHZBqZvr9hAFsqMQ6D9", this can be retrived using the get_for_video() method of this class
            type: str or list of str

        :param textFormat:
            :optional:
            desc: Instruct the API to return the comments left by users in html formatted or in plain text
            :type choice from [html, text]:

        :returns metadata of comment `id`(s) and it's replies.
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "id": kwargs.get('id'),
            "part": "snippet, replies"
        }
        kwargs.pop('id')
        params.update(kwargs)
        
        return "/commentThreads", params

    def get(self, **kwargs) -> tuple:
        """
        Given a comment `id` returns the metadata of that comment without replies.

        Read the docs: https://developers.google.com/youtube/v3/docs/comment/list

        :param id(s):
            :required:
            desc: The ID of a comment i.e. "UgyH6pdCkC_oBCjmm9Z4AaABAg.9hAFHZBqZvr9hAFsqMQ6D9", this can be retrived using the get_for_video() method of this class
            type: str or list of str

        :param maxResults:
            :optional:
            desc: maximum items that should be returned in response
            :type unsigned int:

        :param textFormat:
            :optional:
            desc: Instruct the API to return the comments left by users in html formatted or in plain text
            :type choice from [html, text]:

        :returns metadata of the comment `id` without it's replies.
            "rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "id": kwargs.get('id'),
            "part": "snippet"
        }
        kwargs.pop('id')
        params.update(kwargs)

        return "/comment", params
