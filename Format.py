import yt_dlp
import sys

sys.stdout.reconfigure(encoding='utf-8') 

def get_Info(url):
    ydl_opts = {
        'cookies': 'cookies.txt',
        'nocheckcertificate': True,  # Skip SSL certificate verification
        'format': 'bestvideo+bestaudio/best',  # Select best video and audio
        'merge_output_format': 'mp4',
        'postprocessors': [{                  # Postprocessor for merging
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'          # Preferred output format
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
    return info  

def get_format(url):
    result = list()
    required  = 'manifest_url'
    info = get_Info(url)
    formats = info.get('formats', [])
    for format in formats:
        if required in format:
            result.append(format)
    return result

def get_thumbnail(url):
    required = 'url'
    req = 'width'
    info = get_Info(url)
    thumbnails = info.get('thumbnails')
    for thumbnail in thumbnails:
        if req in thumbnail and required in thumbnail:
            if thumbnail['width'] == 640 :
                return thumbnail['url']