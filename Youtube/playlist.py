# https://developers.google.com/youtube/v3/docs/playlistItems
# https://developers.google.com/youtube/v3/docs/playlists

class Playlist:
    """
    The playlist class handles the methods to fetch data from the YouTube Data API related to a playlist
    """
    def __init__(self):
        pass

    def get(self, **kwargs) -> tuple:
        """
        Given playlist `id`(s) returns metadata (id, title, channelId, videoCount).

        Read the docs: https://developers.google.com/youtube/v3/docs/playlists/list

        :param id:
            :required:
            desc: The ID of a playlist i.e. "PL7mJ5yqSD8wmn40QeT0Au9M1ZjNmgFTTx", this can be found at the end of YouTube urls
            :type str or list of str:

        :returns metadata from givem playlist ``id``s.
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "id": kwargs.get('id'),
            "part": "snippet, contentDetails, id, localizations, status"
        }

        return "/playlists", params
    
    def get_for_channel(self, **kwargs) -> tuple:
        """
        Given a `channelId` returns a list of playlist IDs that `channelId` created.

        Read the docs: https://developers.google.com/youtube/v3/docs/playlists/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of channel's homepage.
            :type str:

        :returns a list of playlist IDs that `channelId` created:
            :rtype tuple:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "channelId": kwargs.get('id'),
            "part": "snippet",
        }
        
        return "/playlists", params

    def get_videos(self, **kwargs) -> tuple:
        """
        Given a `playlistId` returns a list of videos that `playlistId` consists.

        Read the docs: https://developers.google.com/youtube/v3/docs/playlists/list

        :param id:
            :required:
            desc: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of channel's homepage.
            :type str:

        :returns a list of videos that `playlistId` consists:
            :rtype dict:
        """

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params = {
            "playlistId": kwargs.get('id'),
            "part": "snippet, contentDetails, id, status",
        }
        kwargs.pop('id')
        params.update(kwargs)
        
        return "/playlistItems", params
