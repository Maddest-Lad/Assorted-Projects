import os
from PIL import Image

icon_dir = "C:\\Users\\samha\\AppData\\Roaming\\Elgato\\StreamDeck\\IconPacks\\com.samha.stellaris.sdIconPack\\icons"

pngs = [f for f in os.listdir(icon_dir) if f.endswith(".png")]

# Resize all icons to 144x144
for png in pngs:
    im = Image.open(os.path.join(icon_dir, png))
    im = im.resize((330, 290))
    im.save(os.path.join(icon_dir, png))
