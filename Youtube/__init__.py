"""
Pytubedata.py

Simple Youtube Data API Wrapper written in pythn
"""
from .youtube import api
from .endpoints import ENDPOINTS

# Import all libs
from .activities import activities
from .captions import captions
from .channel import channel
from .comments import comment
from .playlist import playlist
from .search import search
from .video import video

# Class client
class Client():

    def __init__(self, key):
        self.key = key

        self.activities= activities(self.key)
        self.captions= captions(key)
        self.channel= channel(key)
        self.comment= comment(key)
        self.playlist= playlist(key)
        self.search= search(key)
        self.video= video(key)