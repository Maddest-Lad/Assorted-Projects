import os
import shutil

from PIL import Image

base_directory = os.getcwd()


# recursively merge two folders including sub-folders
def merge_folders(root_src_dir, root_dst_dir) -> None:
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            if os.path.splitext(file_) != ".json":
                src_file = os.path.join(src_dir, file_)
                dst_file = os.path.join(dst_dir, file_)
                if os.path.exists(dst_file):
                    src_file = combine_images(src_file, dst_file)
                    os.remove(dst_file)
                shutil.copy(src_file, dst_dir)


# combines two images
def combine_images(image_1, image_2) -> str:
    background, foreground = Image.open(image_1), Image.open(image_2)
    background.paste(foreground, (0, 0), foreground)
    background.save(image_1, "PNG")

    return image_1


# Journey Map Data Directories
path_1 = "C:\\Users\\Sam Pc\\PycharmProjects\\JourneyMapCombine\\to_merge\\sam+nathan"
path_2 = "C:\\Users\\Sam Pc\\PycharmProjects\\JourneyMapCombine\\to_merge\\charlie"

merge_folders(path_1, path_2)
shutil.move(path_2, os.path.join(base_directory, "data"))
