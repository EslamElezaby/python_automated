# create youtube download using python

# 1. install git
# 2. install pytube package
# execute the following command: pip install pytube
# for python3, use pip3 instead.


# let's start coding....
from pytube import YouTube
from pytube import Playlist
import os
link = 'https://youtu.be/umDr0mPuyQc'

video = YouTube(link)


# To know info about video like {title , description , length, rating, views}
# print(f"Video Title :\n{video.title}\n_________________________________________________")
# print(f"Video Description :\n{video.description}\n_____________________________________")
# print(f"Video Length :\n {video.length}\n_________________________________________________")

# To know streams (Qualities)
# for stream in video.streams:
#     print(stream)


# You can filter results:
# progressive="True" => it means the video has audio and video.
# progressive="False" => it means the video has just audio.
#
# for stream in video.streams.filter(progressive=True):
#     print(stream)

# get highest or loweest quality
# print(video.streams.get_highest_resolution())
# print(video.streams.get_lowest_resolution())

# Finally to download video
# the dot refers to the current directory
# (the directory of this script).
selected_path = "./downloaded_videos"


def finish():
    path = os.path.realpath(selected_path)
    os.startfile(path)
    print('Download Done')


# After the download finishes, open the folder you selected
video.streams.get_lowest_resolution().download(output_path=selected_path)
video.register_on_complete_callback(finish())

# to download a playlist
# playlist_link = 'https://www.youtube.com/playlist?list=PLDN8vU_ZehsUrlkJ34Rdbsu1VduPvLvvZ'
# playlist = Playlist(playlist_link)
# for video in playlist.videos:
#     video.streams.get_lowest_resolution().download(output_path="./downloaded_videos")

# for more information about pytube,
# visit https://python-pytube.readthedocs.io/en/latest/index.html
