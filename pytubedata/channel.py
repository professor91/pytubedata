from pytubedata.data_models.channel import ChannelData
from pytubedata.playlist_item import PlaylistItem
from pytubedata.playlist import Playlist

from pytubedata.endpoint.playlists import Playlists


class Channel(ChannelData):
    """
    Represents a YouTube Channel
    """
    def __init__(self, data, api_request: object):
        super().__init__(data)
        self._uploads_playlist_id = data['contentDetails']['relatedPlaylists']['uploads']
        self._playlist_endpoint = Playlists(api_request=api_request)

    def get_uploads(self) -> list[PlaylistItem]:
        """
        Gets the uploads playlist for the given YouTube channel
        """
        return self._playlist_endpoint.get_playlist_details(
            playlist_ids=self._uploads_playlist_id
        ).get_playlist_items()

    def get_all_playlists(self) -> list[Playlist]:
        """
        Gets all the playlists of the channel
        """
        return self._playlist_endpoint.get_playlists_by_channel(
            channel_id=self.id
        )

    # TODO: method to get a video (maybe import from video interface class?)
