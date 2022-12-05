import requests
from PIL import Image
from apiclient.discovery import build
from pytube import YouTube
from pydub import AudioSegment
from dataclasses import dataclass

import os

def get_video_data(video_id):
    DEVELOPER_KEY = 'AIzaSyBNgb9cz50JWv6u0ChvKKEloPFC1XsPeXE'
    youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
    return youtube.videos().list(id=video_id, part='snippet').execute().get('items')[0]['snippet']


def save_album_art(url):
    im = Image.open(requests.get(url, stream=True).raw)
    width, height = im.size
    offset = int((width - height) / 2)
    im = im.crop((offset, 0, width - offset, height))
    im.save(fp="AlbumArt.png")

def download_mp3(url):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    return out_file

def time_to_ms(time):
    # Format of XX:YY
    minutes, seconds = time.split(":")
    return int(minutes)*60000 + int(seconds)*1000

@dataclass
class Song:
    name: str
    start_time: int
    end_time: int

def get_songs(description):
    songs = []
    for line in description.split('\n'):
        if line:
            try:
                name = line[line.find(".")+1:line.find("-")]
                timestamps = line[line.find("[")+1:line.find("]")].split("to")

                start_time = time_to_ms(timestamps[0])
                end_time = time_to_ms(timestamps[1])

                songs.append(Song(name, start_time, end_time))
            except:
                continue
    return songs


if __name__ == "__main__":
    url = input("Enter Video URL: ")
    video_id = url.split("v=")[-1]

    video_data = get_video_data(video_id)
    # print(json.dumps(video_data, sort_keys=True, indent=4))

    title, artist, description = video_data['title'], video_data['channelTitle'], video_data['description']
    album_art_url = video_data['thumbnails']['maxres']['url']

    # Save Album Art
    save_album_art(album_art_url)

    # Download MP3, Named "download.mp3"
    filename = download_mp3(url)

    # Extract Song Start/End Times
    songs = get_songs(description)

    # Split Mp3 Into Each Song
    try:
        sound = AudioSegment.from_file(filename, "mp3")
    except:
        sound = AudioSegment.from_file(filename, format="mp4")

    for song in songs:
        current_song = sound[song.start_time:song.end_time]
        current_song.export(f"{song.name}.mp3", format="mp3")
