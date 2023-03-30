API_MAPPER = {
    # Public API Endpoint Functions
    "search": {
        "endpoint": "/search",
        "params": {
            "q": None,
            "part": "snippet",
            "type": ""
        },
        "parse_function": "parse_search_response",
    },
    "activity": {
        "endpoint": "/activities",
        "params": {
            "channelId": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_activity_list_response",
    },

    "channel": {
        "endpoint": "/channels",
        "params": {
            "id": None,
            "part": "snippet, statistics, topicDetails, contentDetails, brandingSettings",
        },
        "parse_function": "parse_channel_response",
    },

    "channel_sections": {
        "endpoint": "/channelSections",
        "params": {
            "channelId": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_channel_section_list_response",
    },

    "channel_section_by_id": {
        "endpoint": "/channelSections",
        "params": {
            "id": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_channel_section_list_response",
    },

    "playlists": {
        "endpoint": "/playlists",
        "params": {
            "channelId": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_playlist_list_response",
    },

    "playlist_by_id": {
        "endpoint": "/playlists",
        "params": {
            "id": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_playlist_list_response",
    },

    "playlist_videos": {
        "endpoint": "/playlistItems",
        "params": {
            "playlistId": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_playlist_video_list_response",
    },

    "playlist_video_by_id": {
        "endpoint": "/playlistItems",
        "params": {
            "id": None,
            "part": "snippet, contentDetails",
        },
        "parse_function": "parse_playlist_video_list_response",
    },

    "video_by_id": {
        "endpoint": "/videos",
        "params": {
            "id": None,
            "part": "contentDetails, id, localizations, snippet, statistics, status, topicDetails",
        },
        "parse_function": "parse_video_response",
    },


    "comments_on_video": {
        "endpoint": "/commentThreads",
        "params": {
            "videoId": None,
            "order": "time",
            "textFormat": "plainText",
        },
        "parse_function": "parse_comments_list_response",
    },
    "replies_to_comment": {
        "endpoint": "/comments",
        "params": {
            "parentId": None,
            "part": "snippet",
            "textFormat": "plainText",
        },
        "parse_function": "parse_comments_list_response",
    },
    "comment_by_id": {
        "endpoint": "/comments",
        "params": {
            "id": None,
            "part": "snippet",
            "textFormat": "plainText",
        },
        "parse_function": "parse_comment_responses",
    },

    "caption": {
        "endpoint": "/captions",
        "params": {
            "videoId": None,
            "part": "snippet",
        },
    },

}
