# https://developers.google.com/youtube/v3/docs/channels
from .youtube import api

class channel(api):
    """
    The channel class handles the methods to fetch data from the YouTube Data API related to a channel

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)
    
    def get(self, id):
        '''
        Given a channel `id` returns metrics (views, subscribersCount, videoCount) and metadata (description, category) as a dictionary.

        Read the docs: https://developers.google.com/youtube/v3/docs/channels/list

        params: required
            id: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            type: str or list of str

        returns metadata from the inputted channel ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "snippet, statistics, topicDetails, brandingSettings, contentDetails, contentOwnerDetails"
        }
        
        return self.request("channel", params)

    def get_all_sections(self, id):
        '''
        Given a channel `id` returns all sections of the channel.

        Read the docs: https://developers.google.com/youtube/v3/docs/channelSections/list

        params: required
            id: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            type: str

        returns sections of the inputted channel ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "channelId": id,
            "part": "snippet, contentDetails"
        }

        return self.request("channel_section", params)

    def get_section(self, id):
        '''
        Given a channelSection `id` return metadata for the section.

        Read the docs: https://developers.google.com/youtube/v3/docs/channelSections/list

        params: required
            id: The ID of a channel section i.e. "UCqW8jxh4tH1Z1sWPbkGWL4g.LeAltgu_pbM", this can be get using get_channel_section() method
            type: str

        returns metadata of the inputted channelSections ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "snippet, contentDetails"
        }

        return self.request("channel_section", params)