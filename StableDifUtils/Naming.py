import os

# specify the directory where your png files are located
directory = 'C:\\Users\\samha\\Desktop\\SD\\Embeddings\\Crafter\\out'

# get a list of all png files in the directory
png_files = [f for f in os.listdir(directory) if f.endswith('.png')]

# loop through the list of png files
for png_file in png_files:
    # create a text file with the same name as the png file
    with open(os.path.join(directory, png_file.replace('.png', '.txt')), 'w') as f:
        # write the name of the png file to the text file
        f.write(png_file.replace(".png", ", Voxel Style"))
