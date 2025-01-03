import yt_dlp
import sys

sys.stdout.reconfigure(encoding='utf-8') 

class Ytdownloader:
    def __init__(self, link):
        self.link = link
        self._info =  self.get_info(link)
        self._formats = self.get_formats()
        self._thumbnail = self.get_thumbnail()
        self._tags = self.get_tags() 
        self._video_format = self.get_video_format()
        self._audio_format = self.get_audio_format()
        self._both = self.get_both()


    @property
    def info(self):
        return self._info
    
    @property
    def formats(self):
        return self._formats
    
    @property
    def thumbnail(self):
        return self._thumbnail
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def video_format(self):
        return self._video_format
    
    @property
    def audio_format(self):
        return self._audio_format
    
    @property
    def both(self):
        return self._both

    def get_info(self,url):
        ydl_opts = {
            'cookies'             : 'cookies.txt',
            'nocheckcertificate'  : True,                          # Skip SSL certificate verification
            'format'              : 'bestvideo+bestaudio/best',    # Select best video and audio
            'merge_output_format' : 'mp4',
            'postprocessors': [{                                   # Postprocessor for merging
                'key'           : 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'                            # Preferred output format
            }]
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
        return info 
    
    def get_formats(self):
        format = []
        information = self.info
        avail_formats = information.get('formats')
        for single_format in avail_formats:
            if 'protocol'in single_format and 'downloader_options' in single_format :
                format.append(single_format)
        return format


    def get_thumbnail(self):
        thumbnail_url = self.info.get('thumbnail')
        return thumbnail_url
    
    def get_tags(self):
        tags  = self.info.get('tags')
        return tags
    
    def get_video_format(self):
        video_format = []
        formats = self.formats
        for single_formats in formats:
            if single_formats['acodec'] == 'none' :
                video_format.append(single_formats)
        return video_format
    
    def get_audio_format(self):
        audio_format = []
        formats =self.formats
        for single_formats in formats:
            if single_formats['vcodec'] == 'none':
                audio_format.append(single_formats)
        return audio_format

    def download(self,url):
        ydl_opts = {
            'cookies'             : 'cookies.txt',
            'nocheckcertificate'  : True,
        }  # No 'format' field
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    def get_both(self):
        both = [] 
        formats =self.formats
        for single_formats in formats:
            if single_formats['vcodec'] != 'none' and single_formats['acodec'] != 'none':
                both.append(single_formats)
        return both
    
    



