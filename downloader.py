from pytube import YouTube


YT = None


def getVideos(url, command=None):
    global YT

    yt = YouTube(url)
    YT = yt
    if command == 'name':
        fn = yt.filename
        print(fn)
    else:
        fn = YT.filename
        videos = yt.filter(extension='mp4')[-1]
        videos = yt.get_videos()
        return videos, fn
        # print(type(videos))


def DL(filename='', destination='', extension='mp4', resolution='720p'):
    if filename != '':
        YT.set_filename(filename)
    vid = YT.get(resolution=resolution, extension=extension)
    vid.download(destination)
