# https://developers.google.com/youtube/v3/docs/search

class Search:
    """
    The search class handles the methods to make search queries on Youtube using YouTube Data API
    """

    def __init__(self):
        pass

    def get(self, **kwargs) -> tuple:
        """
        Given a `query` returns information about a YouTube video, channel, or playlist that matches the search parameters.

        Read the docs: https://developers.google.com/youtube/v3/docs/search/list

        :param query:
            :required:
            desc: The query to be searched for on Youtube
            :type str:

        :param optional:
            Read the docs: https://developers.google.com/youtube/v3/docs/search/list - optional parameters

        :returns metadata from the inputted query ``id``s:
            :rtype dict:
        """

        if not kwargs.get('query'):
            raise KeyError("query not given")

        params = {
            "q": kwargs.get('query'),
            "part": "snippet",
            "type": "video",
        }
        kwargs.pop('query')
        params.update(kwargs)

        return "/search", params
