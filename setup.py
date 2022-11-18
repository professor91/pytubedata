try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open ("README.md", "r") as rf:
    long_description= rf.read()

setup(
    name="pytubedata",
    version="0.0.1",
    description="A simple wrapper for YouTube Data API v3 written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/professor91/pytubedata",
    author="Keshav Saini",
    author_email="keshavandteam@gmail.com",
    packages=["Youtube"],
    keywords=["youtubedata", "youtubedataapi", "pytubedata", "pytubedata.py", "googleapi"],
    install_requires=[
        "requests"
        ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent"
    ],
    # python_requires="~=3.5"
)