import os
import shutil

# Sorts the Downloads Folder into Extension Based Subfolders 
# A Less Ephemeral Version of File Explorer's "Sort by Type"

path =  os.path.expanduser("~") + "/Downloads"

for file in os.listdir(path):

    name, extension = os.path.splitext(file)
    extension = extension[1:]

    # Ignore Shortcuts
    if extension in ["", "lnk"]:
        continue

    destination_folder = os.path.join(path, extension)
    os.makedirs(destination_folder, exist_ok=True)

    try:
        shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))
    except (FileExistsError, PermissionError) as e:
        continue
