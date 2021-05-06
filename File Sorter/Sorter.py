import os
import shutil

# Original By Gaganram PM
# Licenced Under CC BY-NC-SA 4.0 - https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.instructables.com/Automatic-File-Sorter-With-Python/
# Modified By Sam Harris for Readability and Improved Functionality

# A Command Line Script Which Sorts Files Into Sub-Folders Based On File Extension
# Lastly, This Program Ought To Be Migrated To Use the More Up To Date pathlib Library Instead of os.path


# While I'm Not The Biggest Fan of While True, It Facilitates Retrying on Incorrect Inputs
while True:
    try:
        # Get User Input, and Scan The Directory
        path = input("Enter Directory : ")
        files = os.listdir(path)
        break
    except Exception as e:
        print(e)

# Primary Sorting Loop
for file in files:

    # Split the Filenames Up and Extract The Extension
    name, extension = os.path.splitext(file)
    extension = extension[1:]

    # Ignore Any Files Without an Extension, and Those That Cause Errors
    # lnk - The Extension For Shortcuts - Windows Complains About Moving System Links
    if extension in ["", "lnk"]:
        continue

    # End Result Paths
    destination_folder = os.path.join(path, extension)

    # Make The Directory For The File Type, Does Nothing If It's Already There
    os.makedirs(destination_folder, exist_ok=True)

    # Sometimes shutil Can Create All Sorts of Errors - Usually Permission, But Occasionally Wonky Things
    try:
        # The First.txt Path is the Original File's Location + Name, The Second Is The Destination + Name
        shutil.move(os.path.join(path, file), os.path.join(destination_folder, file))
    except (FileExistsError, PermissionError) as e:
        continue
