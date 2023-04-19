from PIL import Image
import numpy as np

# Load the background and foreground images
background = Image.open("background_image.png")
foreground = Image.open("foreground_image.png")

# Resize foreground image to fit the background
foreground = foreground.resize((100, 100))

# Convert both images to RGBA mode to support transparency
background = background.convert("RGBA")
foreground = foreground.convert("RGBA")

# Create a blank image with the same dimensions and mode as the background
combined_image = Image.new("RBGA", background.size)

# Calculate the center coordinates of the combined image
center_x = background.width // 2
center_y = background.height // 2

# Create 8 rotated versions of the foreground image
rotated_images = []
for i in range(8):
    rotated_image = foreground.rotate(i * 45, expand=True)
    rotated_images.append(rotated_image)

# Paste the rotated foreground images onto the combined image
for i in range(8):
    # Calculate the top-left coordinates of the rotated foreground image
    x = center_x - rotated_images[i].width // 2
    y = center_y - rotated_images[i].height // 2

    # Paste the rotated foreground image onto the combined image
    combined_image.alpha_composite(rotated_images[i], (x, y))

# Save the resulting images
combined_image.save("combined_image.png")