import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '0',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage
download_video('https://soundcloud.com/godyssey/moneybags/s-Sy45PjoDZYM')