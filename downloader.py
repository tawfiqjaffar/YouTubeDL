from pytube3 import YouTube

YT = None
 
def findTag(element, tag):
    result = element.find(tag)
    start = element[result:]
    get = False
    res = ""
    index = 0
    for i in range(len(start)):
        if (get):
            res += start[i]
        if (start[i] == '"'):
            get = not get
        if (len(res) != 0 and res[len(res) - 1] == 'p'):
            break
        else:
            continue
    return res
 
 
 
def getVideos(url, command=None):
    global YT
 
    yt = YouTube(url)
    print(yt)
    YT = yt
    result = []
    if command == 'name':
        fn = yt.title
        print(fn)
    else:
        fn = YT.title
        stream = yt.streams
        for el in stream:
            print('el', str(el))
            tag = findTag(str(el), 'res')
            if (tag[0] != 'F' and tag not in result):
                result.append(tag)
        # videos = yt.get_videos()
        print(result)
        return result, fn
        # print(type(videos))
 
 
def DL(resolution):
    stream = YT.streams.get_by_resolution(resolution).all()
    print(stream)
    # vid = YT.get(resolution=resolution, extension=extension)
    # vid.download(destination)