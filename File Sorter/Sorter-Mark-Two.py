import os
from pathlib import Path


def sort_files(path: str, rules: dict, recursive=False) -> list:
    errors = []
    home = Path.home()

    # Get all files in the path
    if recursive:
        files = list(Path(path).rglob('*'))
    else:
        files = list(Path(path).glob('*'))

    # Sort files
    for file in files:
        if file.is_file():
            destination = "sorted"  # Default destination
            for value in rules.values():
                if file.suffix in key:
                    destination = rules[key]
                    break

            # Move file to destination
            try:
                new_location = Path(home / destination)
                os.makedirs(new_location, exist_ok=True)
                print(file.name + " moved to " + new_location)
                # shutil.move(file, Path(new_location / file.name))
            except (FileExistsError, PermissionError) as e:
                errors.append(e)
                continue

    return errors


if __name__ == "__main__":
    log_file = open("log.txt", "w")

    # Get user input for the path to sort
    while True:
        try:
            # Get User Input, and Scan The Directory
            path = input("Enter The Directory You'd Like to Sort : ")
            files = os.listdir(path)
            break
        except Exception as e:
            print(e)

    # The folders it references will be located in your user folder
    rules = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".mpg", ".mpeg"],
        "Documents": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv"],
        "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac", ".m4a"],
        "Midi": [".mid", ".midi"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".h", ".c++", ".php", ".sql", ".json", ".xml"],
        "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"],
        "Applications": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm", ".app", ".appx", ".apk", ".ipa"],
    }

    #sort_files(path, reverse_dictionary)
