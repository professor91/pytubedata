"""
pytubedata.exceptions

This module contains custom exception classes used in the pytubedata package.
"""


class UnauthorizedException(Exception):
    """
    Raised when an API request fails due to invalid or missing API key
    """
    pass


# class RateLimitExceededException(Exception):
#     pass

# Define additional custom exceptions as needed.
