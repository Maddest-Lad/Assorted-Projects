import argparse
import subprocess
import re
from datetime import timedelta
from pathlib import Path

def parse_chapters_from_file(file_path):
    """
    Reads chapters information from a file and parses it into a list of tuples
    with (start_time, title).
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        chapters_text = f.read()
    return parse_chapters(chapters_text)

def parse_chapters(chapters_text):
    """
    Parses a string containing chapter information into a list of tuples
    with (start_time, title).
    """
    chapters = []
    lines = chapters_text.strip().split('\n')
    for line in lines:
        match = re.match(r'(\d{1,2}:\d{2}:\d{2}|\d{1,2}:\d{2})\s(.+)', line)
        if match:
            time_str, title = match.groups()
            chapters.append((time_str, title))
    return chapters

def convert_time_to_seconds(time_str):
    """
    Converts a time string in HH:MM:SS, H:MM:SS, or MM:SS to total seconds.
    """
    parts = time_str.split(':')
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    elif len(parts) == 3:
        return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
    else:
        return 0

def split_video(video_path, chapters, output_dir, audio_quality="192k"):
    """
    Splits the video into separate audio tracks (MP3) based on the chapters.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    for i, (start, title) in enumerate(chapters):
        start_seconds = convert_time_to_seconds(start)
        if i + 1 < len(chapters):
            next_start = chapters[i + 1][0]
            duration = convert_time_to_seconds(next_start) - start_seconds
        else:
            duration = None

        output_filename = f"{i + 1:02d} - {title}.mp3".replace('/', '_').replace('\\', '_')
        output_filepath = output_dir / output_filename

        command = [
            "ffmpeg",
            "-ss", str(timedelta(seconds=start_seconds)),
            "-i", video_path,
            "-vn",
            "-c:a", "libmp3lame",
            "-q:a", "0",
            "-y",
        ]
        if duration:
            command.extend(["-t", str(timedelta(seconds=duration))])
        command.append(str(output_filepath))

        subprocess.run(command, check=True)
        print(f"Chapter '{title}' saved as MP3 to {output_filepath}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a video into MP3 chapters.")
    parser.add_argument("video_path", type=str, help="Path to the input video file.")
    parser.add_argument("chapters_file", type=str, help="Path to the chapters text file.")
    parser.add_argument("output_dir", type=str, help="Directory to save the output MP3 files.")
    args = parser.parse_args()

    chapters = parse_chapters_from_file(args.chapters_file)
    split_video(args.video_path, chapters, args.output_dir)
