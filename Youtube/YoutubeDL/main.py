import youtube_dl

# Put the URL of the YouTube video you want to download in this list
urls = ['https://www.youtube.com/watch?v=VIDEO_ID_1', 'https://www.youtube.com/watch?v=VIDEO_ID_2']

# Set the download options
options = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': '%(title)s.%(ext)s'
}

# Download the videos
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(urls)