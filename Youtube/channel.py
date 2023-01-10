# https://developers.google.com/youtube/v3/docs/channels

class Channel:
    """
    The channel class handles the methods to fetch data from the YouTube Data API related to a channel
    """
    def __init__(self):
        pass

    def get_channel(self, **kwargs):
        """
        Given a channel `id` returns metrics (views, subscribersCount, videoCount) and metadata (description, category) as a dictionary.

        Read the docs: https://developers.google.com/youtube/v3/docs/channels/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            :type str:

        :param maxResults:
            :optional:
            desc: maximum items that should be returned in response
            :type unsigned int:

        :returns metadata of the given channel ``id``:
            :rtype list:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "id": kwargs.get('id'),
            "part": "snippet, statistics, topicDetails, brandingSettings, contentDetails, contentOwnerDetails"
        }
        kwargs.pop('id')

        return "/channels", params

    def get_all_sections(self, **kwargs) -> tuple:
        """
        Given a channel `id` returns all sections of the channel.

        Read the docs: https://developers.google.com/youtube/v3/docs/channelSections/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            :type str:

        :returns all sections of the channel ``id``.
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "channelId": kwargs.get('id'),
            "part": "snippet, contentDetails"
        }
        kwargs.pop('id')
        params.update(kwargs)

        return "/channelSections", params

    def get_section(self, **kwargs):
        """
        Given a channelSection `id` return metadata for the section.

        Read the docs: https://developers.google.com/youtube/v3/docs/channelSections/list

        :param id:
            :required:
            desc: The ID of a channel section i.e. "UCqW8jxh4tH1Z1sWPbkGWL4g.LeAltgu_pbM", this can be get using get_channel_section() method
            :type str:

        :returns metadata of give channel section ``id``s.
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "id": kwargs.get('id'),
            "part": "snippet, contentDetails"
        }
        kwargs.pop('id')
        params.update(kwargs)

        return "/channelSections", params
