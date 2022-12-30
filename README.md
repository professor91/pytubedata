# Pytubedata

Pytubedata is a simple wrapper for [YouTube Data API](https://developers.google.com/youtube/v3) written in python

## Installation

```
pip install pytubedata
```

## Usage
This package requies a valid YT Data API Key. You can get one from [Google Cloud Console](https://console.cloud.google.com/apis/dashboard)


## Quickstart
Getting the `Client` class

```py
from Youtube import client

c= client()
```

## Documentation
- Search for videos
  ```python
    c.request("search", q="search_query")
  ```

- Get details of a channel
  ```python
    c.request("channel_stats", id="channel_id")
  ```

- Get playlists of a channel
  ```python
    c.request("playlists_of_channel", id="channel_id")
  ```

- Get details of a playlist
  ```python
    c.request("playlist_stats", id="playlist_id")
  ```

- Get videos of a playlist
  ```python
    c.request("playlist_videos", id="playlist_id")
   ```

- Get details of a video
  ```python
    c.request("video", id="video_id")
  ```

- Get comments from a video
  ```python
  c.request("comment_for_video", id="video_id")
  ```

- Get replies of a comment
  ```python
    c.request("comment_replies", id="comment_id")
  ```

Check [Youtube Data API Documentation](https://developers.google.com/youtube/v3/docs/) for optional parameters you can pass 


## Contact
Mail: [keshavandteam@gmail.com](mailto:keshavandteam@gmail.com?PyTubeData)