import os
from PIL import Image


def resize_and_pad(img, size):
    # Resize the longest edge of the image to size
    w, h = img.size
    ratio = size / max(w, h)
    new_size = (int(w * ratio), int(h * ratio))
    new_img = img.resize(new_size)

    # Pad the image to create a square
    padding = (
        (size - new_size[0]) // 2,
        (size - new_size[1]) // 2,
    )
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    img.paste(new_img, padding)

    return img


# Set the size for the longest edge
size = 512

# Get the list of all .webp files in the directory
dir_path = 'C:\\Users\\samha\\Desktop\\InvisibleInc\\raw'
files = [f for f in os.listdir(dir_path) if f.endswith('.webp')]

# Loop through each file
for file in files:
    file_path = os.path.join(dir_path, file)
    img = Image.open(file_path)

    # Call the resize_and_pad function
    img = resize_and_pad(img, size)

    # Save the image as PNG
    save_path = os.path.splitext(file_path)[0] + '.png'
    img.save(save_path)
