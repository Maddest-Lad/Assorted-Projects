from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image, text, font=None, font_size=36, position='top', color='white', padding=10):
    # Open the image
    img = Image.open(image)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(img)

    # Set the font and font size
    if font:
        font = ImageFont.truetype(font, font_size)
    else:
        font = ImageFont.load_default()

    # Get the size of the text
    text_size = draw.textsize(text, font=font)

    # Calculate the coordinates for the text
    if position == 'top':
        x = (img.width - text_size[0]) / 2
        y = padding
    elif position == 'bottom':
        x = (img.width - text_size[0]) / 2
        y = img.height - text_size[1] - padding
    else:
        raise ValueError("Invalid value for 'position': {}".format(position))

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=color)

    # Save the modified image
    img.save('modified_image.jpg')


add_text_to_image("download.jpeg", "we do a little bit of bombarding")