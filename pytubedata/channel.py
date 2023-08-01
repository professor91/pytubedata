from pytubedata.data_models import ChannelData


class Channel(ChannelData):
    """
    Represents a YouTube Channel
    """
    def __init__(self, data):
        super().__init__(data)

