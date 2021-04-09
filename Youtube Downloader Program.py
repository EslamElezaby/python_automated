## author => Eslam Elezaby
from pytube import YouTube
from pytube import Playlist
import os

## User Inputs
selected_path = input('Select download path: \n')
# Choice video or playlist
IsPlayListOrVideo = input('What you want to download \n1- video \n2- playlist \n')
# put video link
link = input('Enter video or playlist link :\n')
## choose qulaity
quality = input('What qulaity you want \n 1- Heigthest quality \n 2- Lowerest quality \n')

if IsPlayListOrVideo == '1' :
    video = YouTube(link)
elif IsPlayListOrVideo == '2':
    playlist = Playlist(link)
else:
    print('some error happened')


def finish():
    path = os.path.realpath(selected_path)
    os.startfile(path)
    print('Download Done')

## if user choice video and highest quality
if IsPlayListOrVideo == '1' and quality == '1':
    video.streams.get_highest_resolution().download(output_path=selected_path)
    video.register_on_complete_callback(finish())
## if user choice video and Lowerest quality    
elif IsPlayListOrVideo =='1' and quality == '2':
     video.streams.get_lowest_resolution().download(output_path=selected_path)
     video.register_on_complete_callback(finish())
## if user choice PlayList and highest quality
elif IsPlayListOrVideo == '2' and quality == '1':
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path=selected_path)
    video.register_on_complete_callback(finish())
## if user choice PlayList and highest quality
elif IsPlayListOrVideo == '2' and quality == '2':
    for video in playlist.videos:
        video.streams.get_lowest_resolution().download(output_path=selected_path)
    video.register_on_complete_callback(finish())
else:
    print('some error happened')    
