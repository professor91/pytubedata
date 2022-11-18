# Pytubedata

Pytubedata is a simple wrapper for [YouTube Data API](https://developers.google.com/youtube/v3) written in python

## Installation

```
pip install pytubedata
```

## Usage
This package requies a valid YT Data API Key. You can get one from [Google Cloud Console](https://console.cloud.google.com/apis/dashboard)

## Documentation
[Youtube Data API Documentation](https://developers.google.com/youtube/v3/docs/)

## Quickstart
Getting the `Client` class
```py
from Youtube import Client

key= open("secret.txt", "r").read()
client= Client(key)
```

## Contact
Mail: [keshavandteam@gmail.com](mailto:keshavandteam@gmail.com?PyTubeData)