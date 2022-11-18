# https://developers.google.com/youtube/v3/docs/activities
from .youtube import api

class activities(api):
    """
    The activities class handles the methods to fetch all the activities happened on a channel

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)

    def get_for_channel(self, id, maxResults=50, **kwargs):
        '''
        Given a channel `id` returns the metadata of all actitivies happend on the channel.

        Read the docs: https://developers.google.com/youtube/v3/docs/activities/list

        params: required
            id: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            type: str

        params: optional
            publishedAfter: date and time after which an activity must have occurred for that activity to be included in the API response.
            type: python timestamp object

            publishedBefore: date and time before which an activity must have occurred for that activity to be included in the API response.
            type: python timestamp object

            regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
            type: python timestamp object

        returns metadata of activities from the inputted channel ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "channelId": id,
            "part": "snippet, contentDetails",
            "maxResults": maxResults,
        }
        params.update(kwargs)
        
        return self.request_test("activity", params)