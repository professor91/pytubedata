from pytubedata.data_models.comment_thread import CommentThreadData


class CommentThread(CommentThreadData):
    """
    Represents a YouTube Comment Thread
    """
    def __init__(self, data):
        super().__init__(data)
