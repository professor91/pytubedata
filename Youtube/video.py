# https://developers.google.com/youtube/v3/docs/videos/

class video():
    """
    The video class handles the methods to fetch data from the YouTube Data API related to a video

    params: required
        key- YouTube Data API key. Get a YouTube Data API key here: https://console.cloud.google.com/apis/dashboard
    """
    def __init__(self):
        pass

    def get(self, **kwargs):
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

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params= {
            "id": kwargs.get('id'),
            "part": "contentDetails, id, localizations, snippet, statistics, status, topicDetails",
        }
        kwargs.pop('id')
        params.update(kwargs)
        
        return ("/videos", params)

    def most_popular(self, **kwargs):
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

        if not kwargs.get('regionCode'):
            raise KeyError("regionCode not given")

        if not kwargs.get('videoCategoryId'):
            raise KeyError("videoCategoryId not given")

        params={
            "chart": "mostPopular",
            "regionCode": kwargs.get('regionCode'),
            "videoCategoryId": kwargs.get('videoCategoryId')
        }
        kwargs.pop('regionCode')
        kwargs.pop('videoCategoryId')
        params.update(kwargs)

        return ("/videos", params)

    def get_categories_by_region(self, **kwargs):
        '''
        Given a 'regionCode' returns video category that has been or could be associated with uploaded videos.

        Read the docs: https://developers.google.com/youtube/v3/docs/videoCategories/list

        params: required
            regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
            type: str
        
        returns video categories of inputted `regionCode`
                rtype: dict
        '''

        if not kwargs.get('regionCode'):
            raise KeyError("regionCode not given")


        params= {
            "regionCode": kwargs.get('regionCode'),
            "part": "id, snippet"
        }
        kwargs.pop('regionCode')
        params.update(kwargs)

        return ("/videoCategory", params)

    def get_category_by_id(self, **kwargs):
        '''
        Given a videoCategory `id` returns metadata of the video category.

        Read the docs: https://developers.google.com/youtube/v3/docs/videoCategories/list

        params: required
            regionCode: The parameter value is an ISO 3166-1 alpha-2 country code
            type: str

        returns metadata of the inputted video category `id`
                rtype: dict
        '''

        if not kwargs.get('id'):
            raise KeyError("id not given")

        params= {
            "id": kwargs.get('id'),
            "part": "id, snippet"
        }
        kwargs.pop('id')
        params.update(kwargs)

        return ("/videoCategory", params)