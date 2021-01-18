## create youtube download using python

# 1# install git
# 2# install pytube package
# write this line i your command
# pip install pytube


## let's coding....
from pytube import YouTube
link = 'https://youtu.be/85hKAIMJ6Yk'

video = YouTube(link)


## To Know info about video like {title , description , length, rating, views}
print(f"Video Title :\n{video.title}\n_________________________________________________")
print(f"Video Description :\n{video.description}\n_____________________________________")
print(f"Video Length :\n {video.length}\n_________________________________________________")