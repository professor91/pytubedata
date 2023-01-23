API_MAPPER = {
    # Public API Endpoint Functions
    "activity": {
        "endpoint": "/activities",
        "params": {
            "channelId": None,
            "part": "snippet, contentDetails",
            "maxResults": 10,
        },
    },

    "channel": {
        "endpoint": "/channels",
        "params": {
            "id": None,
            "part": "snippet statistics topicDetails contentDetails brandingSettings",
            "maxResults": 10,
        },
    },

    "channel_sections": {
        "endpoint": "/channelSections",
        "params": {
            "channelId": None,
            "part": "snippet contentDetails",
        },
    },

    "channel_sections_by_id": {
        "endpoint": "/channelSections",
        "params": {
            "id": None,
            "part": "snippet contentDetails",
        },
    },

    "playlists": {
        "endpoint": "/playlists",
        "params": {
            "channelId": None,
            "part": "snippet contentDetails",
            "maxResults": 10,
        },
    },

    "playlists_by_id": {
        "endpoint": "/playlists",
        "params": {
            "id": None,
            "part": "snippet contentDetails",
            "maxResults": 10,
        },
    },

    "playlist_videos": {
        "endpoint": "/playlistItems",
        "params": {
            "playlistId": None,
            "part": "snippet contentDetails",
            "maxResults": 10
        },
    },

    "playlist_videos_by_id": {
        "endpoint": "/playlistItems",
        "params": {
            "id": None,
            "part": "snippet contentDetails",
            "maxResults": 10
        },
    },

    "video_by_id": {
        "endpoint": "/videos",
        "params": {
            "id": None,
            "part": "contentDetails, id, localizations, snippet, statistics, status, topicDetails",
        },
    },


    "comments_on_video": {
        "endpoint": "/commentThreads",
        "params": {
            "videoId": None,
            "maxResults": 100,
            "order": "time",
            "textFormat": "plainText",
        },
    },
    "replies_to_comment": {
        "endpoint": "/comments",
        "params": {
            "parentId": None,
            "part": "snippet",
            "maxResults": 20,
            "textFormat": "plainText",
        }
    },
    "comment_by_id": {
        "endpoint": "/comments",
        "params": {
            "id": None,
            "part": "snippet",
            "textFormat": "plainText",
        }
    },

    "caption": {
        "endpoint": ["/captions"],
        "params": [{
            "videoId": None,
            "part": "snippet",
        }],
    },

}