import pafy
import os
from pytube import Playlist

def download(url):
    video = pafy.new(url)
    audiostreams = video.audiostreams
    print(audiostreams)
    audiostreams[0].download(filepath = "Downloads/"+video.title+".webm")
    import os
    command = 'ffmpeg -i "Downloads/'+video.title+'.webm" -vn -ab 128k -ar 44100 -y "Downloads/'+video.title+'.mp3"'
    os.system(command)
    os.remove("Downloads/"+video.title+".webm")
        

playlist = int(input("Playlist (0) or video (1) or from TXT file (2): "))
if playlist == 0:
    p = Playlist(input("Playlist link: "))
    nb = 1
    print(f"Total of {len(p.video_urls)} videos found")
    for video in p.video_urls:
        download(video)
        print(f"Video nb {nb} downloaded.")
        nb+=1
    print("Done")
        
    
if playlist == 1:
    url = input("Video URL: ")
    download(url)

if playlist == 2:
    with open("TODO.txt","r") as f:
        result = f.readlines()
    for loop in result:
        download(loop.strip())


    
    
