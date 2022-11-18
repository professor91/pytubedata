# https://developers.google.com/youtube/v3/docs/commentThreads
# https://developers.google.com/youtube/v3/docs/comments
from .youtube import api

class comment(api):
    """
    The comment class handles the methods to fetch data from the YouTube Data API related to comments

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)
    
    def get_for_video(self, id, maxResults=50, **kwargs):
        '''
        Given a video `id` returns top level comments on the video.

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        params: required
            id: The ID of a video i.e. "kNbhUWLH_yY", this can be found at the end of YouTube urls
            type: str

        params: optional
            **kwargs:
                order: Specifies the order in which the API response should list comment threads
                type: choice from [time, relevance]
        
                searchTerms: Instructs the API to limit the API response to only contain comments that contain the specified search terms
                type: str
        
                textFormat: Instruct the API to return the comments left by users in html formatted or in plain text
                type: choice from [html, text]
                
        returns top level comments on the inputted videos `id`.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "videoId": id,
            "part": "snippet, replies",
            "maxResults": maxResults
        }
        params.update(kwargs)

        return self.request("comment_thread", params)

    #not working
    def get_for_channel(self, id, maxResults=5, **kwargs):
        '''
        Given a channel `id` returns comment threads containing comments about the specified channel (excluding comments left on videos that the channel uploaded).

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        params: required
            id: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            type: str

        params: optional
            **kwargs:
                order: Specifies the order in which the API response should list comment threads
                type: choice from [time, relevance]
        
                searchTerms: Instructs the API to limit the API response to only contain comments that contain the specified search terms
                type: str
        
                textFormat: Instruct the API to return the comments left by users in html formatted or in plain text
                type: choice from [html, text]
                
        returns top level comments related to the inputted channel `id'.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "channelId": id,
            "part": "snippet, replies",
            "maxResults": maxResults
        }
        params.update(kwargs)
        
        return self.request("comment_thread", params)

    def get_related_to_channel(self, id, maxResults=50, **kwargs):
        '''
        Given a channel `id` returns comment threads associated with the channel(include comments about the channel or about the channel's videos).

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        params: required
            id: The ID of a channel i.e. "UCifqJm4QMYTtrxZb_bN02Pw", this can be found in the source code of homepage of the channel
            type: str

        params: optional
            **kwargs:
                order: Specifies the order in which the API response should list comment threads
                type: choice from [time, relevance]
        
                searchTerms: Instructs the API to limit the API response to only contain comments that contain the specified search terms
                type: str
        
                textFormat: Instruct the API to return the comments left by users in html formatted or in plain text
                type: choice from [html, text]
                
        returns top level comments related to the inputted channel `id`.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "allThreadsRelatedToChannelId": id,
            "part": "snippet, replies",
            "maxResults": maxResults
        }
        params.update(kwargs)
        
        return self.request("comment_thread", params)

    def getr(self, id, **kwargs):
        '''
        Given a commend `id` returns the metadata of that comment with replies.

        Read the docs: https://developers.google.com/youtube/v3/docs/commentThreads/list

        params: required
            id: The ID of a comment i.e. "UgyH6pdCkC_oBCjmm9Z4AaABAg.9hAFHZBqZvr9hAFsqMQ6D9", this can be retrived using the get_for_video() method of this class
            type: str

        params: optional
            **kwargs:                
                textFormat: Instruct the API to return the comments left by users in html formatted or in plain text
                type: choice from [html, text]
                
        returns metadata of the comment `id`.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "snippet, replies"
        }
        params.update(kwargs)
        
        return self.request("comment_thread", params)

    def get(self, id, **kwargs):
        '''
        Given a commend `id` returns the metadata of that comment without replies.

        Read the docs: https://developers.google.com/youtube/v3/docs/comment/list

        params: required
            id: The ID of a comment i.e. "UgyH6pdCkC_oBCjmm9Z4AaABAg.9hAFHZBqZvr9hAFsqMQ6D9", this can be retrived using the get_for_video() method of this class
            type: str

        params: optional
            **kwargs:                
                textFormat: Instruct the API to return the comments left by users in html formatted or in plain text
                type: choice from [html, text]
                
        returns metadata of the comment `id`.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "snippet"
        }
        params.update(kwargs)

        return self.request_test("comment", params)