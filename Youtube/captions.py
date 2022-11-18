# https://developers.google.com/youtube/v3/docs/captions
from .youtube import api

class captions(api):
    """
    The captions class handles the methods to fetch captions of a video from the YouTube Data API

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)
    
    def get_of_video(self, id):
        '''
        Given a video `id` returns the metadata of all the captions of that video.

        Read the docs: https://developers.google.com/youtube/v3/docs/captions/list

        params: required
            id: The ID of a video i.e. "kNbhUWLH_yY", this can be found at the end of YouTube urls
            type: str

        returns metadata from the inputted channel ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "videoId": id,
            "part": "snippet",
        }

        return self.request_test("caption", params)