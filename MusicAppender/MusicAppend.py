import os
import subprocess

# Set the path to the intro and loop files, and the output directory
ost_dir = "C:\\Users\\samha\\Desktop\\DeadCells_Castlevania_Music"
output_path = "C:\\Users\\samha\\PycharmProjects\\Assorted-Projects\\MusicAppender\\out"


# Get a list of all the intro and loop files that match the substring
intro_files = [f for f in os.listdir(ost_dir) if f.endswith(f"_intro.ogg")]
loop_files = [f for f in os.listdir(ost_dir) if f.endswith(f"_loop.ogg")]

# Loop through all the intro files and find the corresponding loop file
for intro_file in intro_files:
    for loop_file in loop_files:
        if intro_file.rsplit("_", 1)[0] == loop_file.rsplit("_", 1)[0]:
            output_file = intro_file.replace("_intro", "")
            intro_file_path = os.path.join(ost_dir, intro_file)
            loop_file_path = os.path.join(ost_dir, loop_file)
            output_file_path = os.path.join(output_path, output_file)
            print(loop_file, intro_file)
            subprocess.run(["ffmpeg", "-i", intro_file_path, "-i", loop_file_path, "-filter_complex", "[0:a] [1:a] concat=n=2:v=0:a=1 [a]", "-map", "[a]", output_file_path])
