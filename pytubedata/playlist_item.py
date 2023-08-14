from pytubedata.data_models.playlist_item import PlaylistItemData
from pytubedata.endpoint.videos import Videos


class PlaylistItem(PlaylistItemData):
    """
    Represents a YouTube Playlist Item (video)
    """
    def __init__(self, data, api_request: object):
        super().__init__(data)
        self._video_endpoint = Videos(api_request)

    def get_video(self):
        """
        Get the video details
        """
        self._video_endpoint.get_video_details(self.video_id)
