# https://developers.google.com/youtube/v3/docs/activities

class Activities:
    """
    The activities class handles the methods to fetch all the activities happened on a channel
    """
    def __init__(self):
        pass

    @classmethod
    def get_for_channel(cls, **kwargs) -> tuple:
        """
        Given a channel `id` returns the metadata of all activities happened on the channel.

        Read the docs: https://developers.google.com/youtube/v3/docs/activities/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            :type str:

        :param maxResults:
            :optional:
            desc: maximum items that should be returned in response
            :type unsigned int:

        :param publishedAfter:
            :optional:
            desc: date and time after which an activity must have occurred for that activity to be included in the API response.
            :type python timestamp object:

        :param publishedBefore:
            :optional:
            desc: date and time before which an activity must have occurred for that activity to be included in the API response.
            :type python timestamp object:

        :param regionCode:
            :optional:
            desc: The parameter value is an ISO 3166-1 alpha-2 country code
            :type python timestamp object:

        :returns metadata of community activity of given channel ``id``.
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "channelId": kwargs.get('id'),
            "part": "snippet, contentDetails",
        }
        kwargs.pop('id')
        params.update(kwargs)

        return '/activities', params
