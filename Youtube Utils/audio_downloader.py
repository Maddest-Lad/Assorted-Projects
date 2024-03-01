import argparse
from pathlib import Path
import subprocess
import re
import os

from pytubefix import YouTube

def sanitize_filename(filename):
    """
    Remove or replace characters that aren't allowed in filenames
    """
    # Remove invalid characters
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    
    # Remove leading/trailing dots and spaces, replace periods with underscores
    filename = filename.strip('. ').replace('.', '_')

    return filename

def download(url: str, media_library_path: Path) -> str:
    """
    url: URL of the video to download
    media_library_path: working directory for media library 
    """
    yt = YouTube(url)
    metadata = {}

    # Confirm Valid Video
    try:
        yt.check_availability()
    except Exception as e:
        print(f"Video Unavailable: {e}")
        return f"The Video is Unavailable, Reason: {str(e)}"

    # Gather video metadata information to bake in with FFmpeg
    metadata['artist'] = sanitize_filename(yt.author)
    metadata['title'] = sanitize_filename(yt.title)
    metadata['published'] = yt.publish_date.strftime("%Y-%m-%d")
    metadata['year'] = str(yt.publish_date.year)
    
    # Filename & metadata info
    output_path = media_library_path / metadata['artist']

    # Download the best adaptive audio track
    audio = Path(yt.streams.filter(only_audio=True).order_by('abr').last().download(filename="audio", output_path=output_path))
   
    # Merge the metadata and audio with ffmpeg 
    try:  
        return convert_with_ffmpeg(audio, metadata, output_path)
    finally:
        # Delete the temporary files
        if audio.exists():
            audio.unlink()

def convert_with_ffmpeg(input_audio: Path, metadata: dict, output_path: Path):
    output_audio = output_path / f"{metadata['title']}.mp3"

    # Convert MP4 to MP3 using FFmpeg
    command = [
        "ffmpeg",
        "-i", str(input_audio),
        "-vn",
        "-acodec", "libmp3lame", # Use MP3 encoding
    ]
    
    # Add the metadata, potentially with additional sanitization if necessary
    for key, value in metadata.items():
        if value:
            command.extend(["-metadata", f"{key}={value}"])

    # Construct the output file name and extend the command
    output_file = Path(f"{metadata['title']}.mp3")
    output_full_path = output_path / output_file

    # Add the output file to the command
    command.extend([str(output_full_path)]) 

   # Run the ffmpeg command
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        return "Video Downloaded and Merged Successfully"
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return "An error occurred during the video processing." 
    
if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Download YouTube video, audio, or both with optional subtitles.')

    # Add arguments
    parser.add_argument('url', help='URL of the YouTube video')
    parser.add_argument('--path', type=Path, help='Path to save the downloaded media', default=Path.cwd())

    # Parse arguments
    args = parser.parse_args()

    result_message = download(url=args.url, media_library_path=args.path)
    print(result_message)