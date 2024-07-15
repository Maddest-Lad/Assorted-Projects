import khinsider
from pathlib import Path

name = input("Enter the name of the album: ")

khinsider.download(name, path=Path(name), formatOrder=['flac', 'ogg', 'mp3'])
