import os
from moviepy.video.io.VideoFileClip import VideoFileClip

total_duration = 0

# Replace "/path/to/folder" with the path to your folder
for root, dirs, files in os.walk(r"E:\Embeddedahmedabelraoef\04 GPIO Module Explanation (PIC Microcontroller)"):
    for file in files:
        if file.endswith(".mp4"):
            filepath = os.path.join(root, file)
            clip = VideoFileClip(filepath)
            total_duration += clip.duration
		
            clip.close()

print("Total duration of all MP4 files:", total_duration/3600, "hours")

input("Press Enter to exit...")
