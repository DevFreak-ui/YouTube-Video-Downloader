from django.shortcuts import render, HttpResponse
from pytube import YouTube
from datetime import timedelta
import os


# Create your views here.


def index(request):
    return render(request, 'index.html', {'title': ''})


def convert(request):
    if request.method == "POST":
        global url
        global title
        url = request.POST['url']
        yt = YouTube(url)
        title = yt.title
        thumbnail_url = yt.thumbnail_url
        time = timedelta(seconds=yt.length)

        videos = yt.streams.filter(progressive=True, file_extension='mp4').desc()
        video_list = []
        for video in videos:
            video_info = []
            resolution = video.resolution
            itag = video.itag
            vid_size = round(video.filesize/(1024*1024))
            video_info.append(resolution)
            video_info.append(vid_size)
            video_info.append(itag)
            video_list.append(video_info)
        
        audios = yt.streams.filter(only_audio=True).desc()
        audio_list = []

        for audio in audios:
            audio_info = []
            quality = audio.abr
            itag = audio.itag
            audio_size = round(audio.filesize/(1024*1024))
            audio_info.append(quality)
            audio_info.append(audio_size),
            audio_info.append(itag)
            audio_list.append(audio_info)
        
    
        details = {
            'title': title, 
            'thumbnail': thumbnail_url, 
            'videos': video_list, 
            'audios': audio_list, 
            'time': time
            }
        return render(request, 'index.html', details)


def download(request):
    global url
    itag = request.GET['itag']
    st = YouTube(url).streams.get_by_itag(itag)

    base, ext = os.path.splitext(st.default_filename)
    new_file_name = base + '_{}'.format(itag) + ext
    
    homedir = os.path.expanduser('~')
    dir = homedir + '/Downloads/'

    st.download(output_path=dir, filename=new_file_name)
    return HttpResponse('Thanks for using Diva')
    


def documentation(request):
    return HttpResponse('Under construction')