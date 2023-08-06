from pytubedata.data_models.video import VideoData


class Video(VideoData):
    """
    Represents a YouTube Video
    """
    def __init__(self, data):
        super().__init__(data)
