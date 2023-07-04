import os
from datetime import date
from moviepy.editor import VideoFileClip

# Define the path to the folder containing the MP4 videos
videos_folder = "E:\Embeddedahmedabelraoef"

# Get today's date
today = date.today()

# Create a timestamp for today's date
timestamp = today.strftime("%Y-%m-%d")

# Create a filename for the log
log_filename = f"E:/playtime_{timestamp}.txt"

total_playtime = 0

# Recursively iterate through the folder and its subfolders
for root, dirs, files in os.walk(videos_folder):
    for file in files:
        # Check if the file is an MP4 video
        if file.endswith(".mp4"):
            # Get the full path of the video file
            video_file = os.path.join(root, file)

            # Load the MP4 file
            video = VideoFileClip(video_file)

            # Get the duration of the video in seconds
            video_duration = video.duration

            # Add the duration to the total playtime
            total_playtime += video_duration

# Open the log file in append mode
with open(log_filename, "a") as log_file:
    # Write the total playtime for today's date
    log_file.write(f"{timestamp}: {total_playtime} seconds\n")
