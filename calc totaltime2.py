import os
from moviepy.video.io.VideoFileClip import VideoFileClip

folder_path = input("Enter the folder path: ")

total_duration = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".mp4"):
            filepath = os.path.join(root, file)
            clip = VideoFileClip(filepath)
            total_duration += clip.duration
            clip.close()

print("Total duration of all MP4 files:", total_duration / 3600, "hours")

input("Press Enter to exit...")
