FUNCTION_CLASS_METHOD_MAP= {
    # Public API Endpoint Functions
    "activity_for_channel" :
        {
            'class': 'activities',
            'class_method': 'get_for_channel'
            },

    "caption_of_video":
        {
            'class': 'captions',
            'class_method': 'get_of_video'
            },

    "channel_stats":
        {
            'class': 'channel',
            'class_method': 'get_channel'
            },
    "channel_all_sections":
        {
            'class': 'channel',
            'class_method': 'get_all_sections'
        },
    "channel_section":
        {
            'class': 'channel',
            'class_method': 'get_section'
        },

    "comment_for_video":
        {
            'class': 'comment',
            'class_method': 'get_for_video'
        },
    "comment_for_channel":
        {
            'class': 'comment',
            'class_method': 'get_for_channel'
        },
    "comment_related_to_channel":
        {
            'class': 'comment',
            'class_method': 'get_related_to_channel'
        },
    "comment_replies":
        {
            'class': 'comment',
            'class_method': 'getr'
        },
    "comment_stats":
        {
            'class': 'comment',
            'class_method': 'get'
        },

    "playlist_stats":
        {
            'class': 'playlist',
            'class_method': 'get'
        },
    "playlists_of_channel":
        {
            'class': 'playlist',
            'class_method': 'get_for_channel'
        },
    "playlist_videos":
        {
            'class': 'playlist',
            'class_method': 'get_videos'
        },

    "search":
        {
            'class': 'search',
            'class_method': 'get'
        },

    "video":
        {
            'class': 'video',
            'class_method': 'get'
        },
    "most_popular_videos":
        {
            'class': 'video',
            'class_method': 'most_popular'
        }
}