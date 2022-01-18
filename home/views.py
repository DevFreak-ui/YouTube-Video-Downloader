from django.shortcuts import render, HttpResponse
from pytube import YouTube
from django.http import JsonResponse
from datetime import timedelta


# Create your views here.


def index(request):
    return render(request, 'index.html', {'title': ''})


def watch(request):
    url = request.GET['url']
    yt = YouTube(url)
    title = yt.title
    thumbnail_url = yt.thumbnail_url
    time = timedelta(seconds=yt.length)

    videos = yt.streams.filter(progressive=True).desc()
    video_list = []
    for video in videos:
        video_info = []
        resolution = video.resolution
        vid_size = round(video.filesize/(1024*1024))
        video_info.append(resolution)
        video_info.append(vid_size)
        video_info.append(url)
        video_list.append(video_info)
    
    audios = yt.streams.filter(only_audio=True).desc()
    audio_list = []
    for audio in audios:
        audio_info = []
        quality = audio.abr
        audio_size = round(audio.filesize/(1024*1024))
        audio_info.append(quality)
        audio_info.append(audio_size)
        audio_info.append(url)
        audio_list.append(audio_info)
    
   
    details = {'title': title, 'thumbnail': thumbnail_url, 'videos': video_list, 'audios': audio_list, 'time': time}
    return render(request, 'index.html', details)


def download(request):
    url = request.GET['url']
    res = request.GET['res']
    st = YouTube(url).streams.filter(resolution=res).first()
    return st.download()


def documentation(request):
    return HttpResponse('Under construction')