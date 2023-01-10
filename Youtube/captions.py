# https://developers.google.com/youtube/v3/docs/captions

class Captions:
    """
    The captions class handles the methods to fetch captions of a video from the YouTube Data API
    """
    def __init__(self):
        pass

    def get_of_video(self, **kwargs) -> tuple:
        """
        Given a video `id` returns the metadata of all the captions of that video.

        Read the docs: https://developers.google.com/youtube/v3/docs/captions/list

        :param id:
            :required:
            desc: The ID of a video i.e. "kNbhUWLH_yY", this can be found at the end of YouTube urls
            :type str:

        :param caption_id:
            :optional:
            desc: List of Ids of captions
            :type list:

        :returns metadata of captions of given video ``id``:
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "videoId": kwargs.get('id'),
            "part": "snippet",
        }
        kwargs.pop('id')
        params.update(kwargs)

        return '/captions', params
