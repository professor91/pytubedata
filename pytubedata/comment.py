from pytubedata.data_models import CommentData


class Comment(CommentData):
    """
    Represents a YouTube Comment
    """
    def __init__(self, data):
        super().__init__(data)
