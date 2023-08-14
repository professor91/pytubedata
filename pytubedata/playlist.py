from pytubedata.data_models.playlist import PlaylistData

from pytubedata.endpoint.playlist_items import PlaylistItems, PlaylistItem


class Playlist(PlaylistData):
    """
    Represents a YouTube Playlist
    """
    def __init__(self, data, api_request: object):
        super().__init__(data)
        self._playlist_item_endpoint = PlaylistItems(api_request=api_request)

    def get_playlist_items(self) -> list[PlaylistItem]:
        return self._playlist_item_endpoint.get_playlist_items(self.id)
