from pytubedata.data_models import PlaylistData


class Playlist(PlaylistData):
    """
    Represents a YouTube Playlist
    """
    def __init__(self, data):
        super().__init__(data)
