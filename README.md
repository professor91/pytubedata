# Pytubedata

Pytubedata is a simple wrapper for [YouTube Data API](https://developers.google.com/youtube/v3) written in python

## Installation

```
pip install pytubedata
```

## Usage
This package requies a valid YT Data API Key. You can get one from [Google Cloud Console](https://console.cloud.google.com/apis/dashboard).


## Quickstart
- Create a file in `secret.yml` in the project's root directory and save the YouTube Data API key in that file.


- Getting the `Client`
  ```python
  from Youtube import Client

  c= Client()
  ```

## Documentation
- Search for videos (not supported)
  ```python
    c.request("search", q="search_query")
  ```

- Get activities of a channel
  ```python
    c.request("activity", id="channel_id")
  ```

- Get details of a channel
  ```python
    c.request("channel", id="channel_id")
  ```

- Get sections of a channel
  ```python
    c.request("channel_sections", id="channel_id")
  ```

- Get section of a channel by id
  ```python
    c.request("channel_section_by_id", id="channel_id")
  ```

- Get playlists of a channel
  ```python
    c.request("playlists", id="channel_id")
  ```

- Get playlist of a channel by id
  ```python
    c.request("playlist_by_id", id="playlist_id")
  ```

- Get videos of a playlist
  ```python
    c.request("playlist_videos", id="playlist_id")
  ```

- Get details of a video by id 
  ```python
    c.request("video_by_id", id="video_id")
   ```

- Get comments on a video
  ```python
  c.request("comments_on_video", id="video_id")
  ```

- Get replies of a comment
  ```python
    c.request("replies_to_comment", id="comment_id")
  ```

- Get comment details by id
  ```python
    c.request("comment_by_id", id="comment_id")
  ```

[//]: # (Check [Youtube Data API Documentation]&#40;https://developers.google.com/youtube/v3/docs/&#41; for optional parameters you can pass )


## Contact
Mail: [keshavandteam@gmail.com](mailto:keshavandteam@gmail.com?PyTubeData)