from pathlib import Path
import subprocess
import re
import os

from pytube import YouTube

def sanitize_filename(filename):
    """
    Remove or replace characters that aren't allowed in filenames
    """
    # Remove invalid characters
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    
    # Remove leading/trailing dots and spaces, replace periods with underscores
    filename = filename.strip('. ').replace('.', '_')

    return filename

def download_video(url: str, media_library_path: Path, include_subtitles: bool = False) -> str:
    """
    url: URL of the video to download
    media_library_path: working directory for media library 
    include_subtitles: Bool detirmining whether or not to download them
    """
    yt = YouTube(url)
    metadata = {}

    # Confirm Valid Video
    try:
        yt.check_availability()
    except Exception as e:
        print(f"Video Unavailable: {e}")
        return f"The Video is Unavailable, Reason: {str(e)}"

    # Gather video metadata information to bake in with FFmpeg # TODO still needs some work for MKV tags
    metadata['studio'] = sanitize_filename(yt.author)
    metadata['title'] = sanitize_filename(yt.title)
    metadata['rating'] = yt.rating
    metadata['published'] = yt.publish_date.strftime("%Y-%m-%d")
    metadata['year'] = yt.publish_date.year
    
    # Filename & metadata info
    output_path = media_library_path / metadata['studio']

    # Download the best adaptive video and audio tracks # TODO store these using tempfile instead of on disk 
    input_video = Path(yt.streams.filter(only_video=True).order_by('resolution').last().download(filename="video", output_path=output_path))
    input_audio = Path(yt.streams.filter(only_audio=True).order_by('abr').last().download(filename="audio", output_path=output_path))

    # Download SRT Subtitles
    input_subtitles = None
    if include_subtitles and yt.captions:
        # Define a priority list of preferred caption languages
        preferred_languages = ['en', 'en-us', 'a.en'] # Note "a.en" is Youtube Auto-Generated

        # Loop through the preferred languages and download the first available one
        for lang in preferred_languages:
            if lang in yt.captions:
                input_subtitles = Path(yt.captions[lang].download(title=metadata['title'], output_path=output_path))
                break
    
    # Merge everything together with ffmpeg 
    try:  
        return combine_with_ffmpeg(input_video, input_audio, input_subtitles, metadata, output_path)
    finally:
        # Delete the temporary files
        if input_video.exists():
            input_video.unlink()
        if input_audio.exists():
            input_audio.unlink()

# Uses FFMPEG to Combine the Video, Audio & Subtitle Tracks Together - Alongside Metadata
def combine_with_ffmpeg(input_video: Path, input_audio: Path, input_subtitles: Path, metadata: dict, output_path: Path):

    command = [
        "ffmpeg"
    ]

    # Check if we have a subtitle file to include
    if input_subtitles:
        command.extend(["-i", input_subtitles])

    # Add Audio & Video
    command.extend([
        "-i", input_video,
        "-i", input_audio,
    ])

    # Add the metadata
    for key, value in metadata.items():
        if value:  # Check if the value is not None or empty, otherwise, it's skipped
            command.extend(["-metadata", f"{key}={value}"])

    # Construct the output file name and extend the command
    output_file = Path(f"{metadata['title']}.mkv")
    output_full_path = output_path / output_file

    # Copy Attributes
    command.extend([
        "-c:v", "copy",
        "-c:a", "copy",
        output_full_path,
        "-y" # Allow Overwritting
    ])

    # Run the ffmpeg command
    try:
        subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        return "Video Downloaded and Merged Successfully"
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        return "An error occurred during the video processing." 
    
if __name__ == "__main__":
    download_video(url=input("Enter Video Url: "), media_library_path=Path.cwd())