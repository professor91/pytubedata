# https://developers.google.com/youtube/v3/docs/captions

class captions():
    """
    The captions class handles the methods to fetch captions of a video from the YouTube Data API

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self):
        pass

    def get_of_video(self, **kwargs):
        '''
        Given a video `id` returns the metadata of all the captions of that video.

        Read the docs: https://developers.google.com/youtube/v3/docs/captions/list

        params: required
            id: The ID of a video i.e. "kNbhUWLH_yY", this can be found at the end of YouTube urls
            type: str

        returns metadata from the inputted channel ``id``s.
                rtype: dict
        '''

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params= {
            "videoId": kwargs.get('id'),
            "part": "snippet",
        }
        kwargs.pop('id')
        params.update(kwargs)

        return ('/captions', params)
