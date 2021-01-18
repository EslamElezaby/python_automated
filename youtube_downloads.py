## create youtube download using python

# 1# install git
# 2# install pytube package
# write this line i your command
# pip install pytube


## let's coding....
from pytube import YouTube
from pytube import Playlist
import os
link = 'https://youtu.be/umDr0mPuyQc'

video = YouTube(link)


## To Know info about video like {title , description , length, rating, views}
# print(f"Video Title :\n{video.title}\n_________________________________________________")
# print(f"Video Description :\n{video.description}\n_____________________________________")
# print(f"Video Length :\n {video.length}\n_________________________________________________")

## To Know streams (Qualities)
# for stream in video.streams:
#     print(stream)

## progressive="True" => it means video have audio and video.
## progressive="False" => it means video have just audio.

## You can filter results
# for stream in video.streams.filter(progressive=True):
#     print(stream)

## get hightest quality or lower quality
# print(video.streams.get_highest_resolution())
# print(video.streams.get_lowest_resolution())

# Finally to download video
selected_path = "E:/"
def finish():
    path = os.path.realpath(selected_path)
    os.startfile(path)
    print('Download Done')


## After download will automated oping folder you seleted
video.streams.get_lowest_resolution().download(output_path=selected_path)
video.register_on_complete_callback(finish())

## download playlist
# playlist_link = 'https://www.youtube.com/playlist?list=PLDN8vU_ZehsUrlkJ34Rdbsu1VduPvLvvZ'
# Playlist = Playlist(playlist_link)
# for video in Playlist.videos:
#     video.streams.get_lowest_resolution().download(output_path="E:/")

## for more information about pytube visit
# link => https://python-pytube.readthedocs.io/en/latest/index.html    




