# https://developers.google.com/youtube/v3/docs/playlistItems
# https://developers.google.com/youtube/v3/docs/playlists
from .youtube import api

class playlist(api):
    """
    The playlist class handles the methods to fetch data from the YouTube Data API related to a playlist

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)

    def get(self, id):
        '''
        Given playlist `id`(s) returns metadata (id, title, channelId, videoCount).

        Read the docs: https://developers.google.com/youtube/v3/docs/playlists/list

        params: required
            id: The ID of a playlist i.e. "PL7mJ5yqSD8wmn40QeT0Au9M1ZjNmgFTTx", this can be found at the end of YouTube urls
            type: str or list of str

        returns metadata from the inputted playlist ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "snippet, contentDetails, id, localizations, status"
        }

        return self.request("playlist", params)
    
    def get_for_channel(self, channelId, maxResult=50):
        '''
        Given a `channelId` returns a list of playlist IDs that `channelId` created.

        Read the docs: https://developers.google.com/youtube/v3/docs/playlists/list

        params: required
            channelId: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of channel's homepage.
            type: str
        
        returns a list of playlist IDs that `channelId` created
                rtype: dict
        '''
        params= {
            "key": self.key,
            "part": "snippet",
            "channelId": channelId,
            "maxResult": maxResult
        }
        
        return self.request("playlist", params)

    def get_videos(self, id, maxResult=50):
        '''
        Given a `channelId` returns a list of playlist IDs that `channelId` created.

        Read the docs: https://developers.google.com/youtube/v3/docs/playlists/list

        params: required
            channelId: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of channel's homepage.
            type: str
        
        returns a list of playlist IDs that `channelId` created
                rtype: dict
        '''
        params= {
            "key": self.key,
            "playlistId": id,
            "part": "snippet, contentDetails, id, status",
            "maxResult": maxResult
        }
        
        return self.request("playlist_item", params)