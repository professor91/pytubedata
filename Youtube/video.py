# https://developers.google.com/youtube/v3/docs/videos/
from .youtube import api

class video(api):
    """
    The video class handles the methods to fetch data from the YouTube Data API related to a video

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self, key):
        super().__init__(key)
    
    def get(self, id, maxResults= 10, **kwargs):
        '''
        Given a video `id` returns metrics (views, likes, comments) and metadata (description, category) as a dictionary.

        Read the docs: https://developers.google.com/youtube/v3/docs/videos/list

        params: required
            id: The ID of a video i.e. "kNbhUWLH_yY", this can be found at the end of YouTube urls
            type: str or list of str

        params: optional
            **kwargs: 
                regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
                type: str

                videoCategoryId
        
        returns metadata from the inputted video ``id``s.
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "contentDetails, id, localizations, snippet, statistics, status, topicDetails",
            "maxResults": maxResults
        }
        params.update(kwargs)
        
        return self.request("video", params)

    def most_popular(self, regionCode, videoCategoryId, **kwargs):
        '''
        Given a `regionCode` and `videoCategoryId` returns most popular videos for the specifies region and video category.

        Read the docs: https://developers.google.com/youtube/v3/docs/videos/list

        params: required
            regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
            type: str

        params: optional
            **kwargs: 
                regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
                type: str
                
                videoCategoryId:
                type: str

        
        returns metadata from the inputted video ``id``s.
                rtype: dict
        '''
        params={
            "key": self.key,
            "chart": "mostPopular",
            "regionCode": regionCode,
            "videoCategoryId": videoCategoryId
        }
        params.update(kwargs)

        return self.request("video", params)

    def get_categories_by_region(self, regionCode="IN"):
        '''
        Given a 'regionCode' returns video category that has been or could be associated with uploaded videos.

        Read the docs: https://developers.google.com/youtube/v3/docs/videoCategories/list

        params: required
            regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
            type: str
        
        returns video categories of inputted `regionCode`
                rtype: dict
        '''
        params= {
            "key": self.key,
            "regionCode": regionCode,
            "part": "id, snippet"
        }

        return self.request_test("video_category", params)

    def get_category_by_id(self, id):
        '''
        Given a videoCategory `id` returns metadata of the video category.

        Read the docs: https://developers.google.com/youtube/v3/docs/videoCategories/list

        params: required
            regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
            type: str

        returns metadata of the inputted video category `id`
                rtype: dict
        '''
        params= {
            "key": self.key,
            "id": id,
            "part": "id, snippet"
        }

        return self.request_test("video_category", params)