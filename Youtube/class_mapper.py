FUNCTION_CLASS_METHOD_MAP= {
    # Public API Endpoint Functions
    "activity_for_channel" :
        {
            'class': 'Activities',
            'class_method': 'get_for_channel'
            },

    "caption_of_video":
        {
            'class': 'Captions',
            'class_method': 'get_of_video'
            },

    "channel_stats":
        {
            'class': 'Channel',
            'class_method': 'get_channel'
            },
    "channel_all_sections":
        {
            'class': 'Channel',
            'class_method': 'get_all_sections'
        },
    "channel_section":
        {
            'class': 'Channel',
            'class_method': 'get_section'
        },

    "comment_for_video":
        {
            'class': 'Comment',
            'class_method': 'get_for_video'
        },
    "comment_for_channel":
        {
            'class': 'Comment',
            'class_method': 'get_for_channel'
        },
    "comment_related_to_channel":
        {
            'class': 'Comment',
            'class_method': 'get_related_to_channel'
        },
    "comment_replies":
        {
            'class': 'Comment',
            'class_method': 'getr'
        },
    "comment_stats":
        {
            'class': 'Comment',
            'class_method': 'get'
        },

    "playlist_stats":
        {
            'class': 'Playlist',
            'class_method': 'get'
        },
    "playlists_of_channel":
        {
            'class': 'Playlist',
            'class_method': 'get_for_channel'
        },
    "playlist_videos":
        {
            'class': 'Playlist',
            'class_method': 'get_videos'
        },

    "search":
        {
            'class': 'Search',
            'class_method': 'get'
        },

    "video":
        {
            'class': 'Video',
            'class_method': 'get'
        },
    "most_popular_videos":
        {
            'class': 'Video',
            'class_method': 'most_popular'
        }
}