# Write a python script that when you import a video file, it will do two commands 
# from:https://ostechnix.com/20-ffmpeg-commands-beginners/(you can use any other commands as well, as long as both use ffmpeg)

import subprocess

# Input video file path
input_file = ""

# Command 1: Convert video to GIF
command1 = ["ffmpeg", "-i", input_file, "-vf", "scale=320:-1", "-t", "10", "-r", "10", "output.gif"]
subprocess.run(command1)

# Command 2: Extract audio from video
command2 = ["ffmpeg", "-i", input_file, "-vn", "-acodec", "copy", "output.mp3"]
subprocess.run(command2)
