import yt_dlp

url = input("URL YouTube: ")

options = {
    "format": "bestaudio/best",
    "outtmpl": "%(title)s.%(ext)s",
    "js_runtimes": {"node": {}},
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])