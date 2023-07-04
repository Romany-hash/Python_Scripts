import os
import shutil

# set the source path and new folder path
source_path = 'E:/lynda learning/[TutsNode.net] - Automobile Vulnerability and Security v1.0'
new_folder_path = 'E:/lynda learning/Automobile hacking'

# create the new folder if it doesn't already exist
if not os.path.exists(new_folder_path):
    os.mkdir(new_folder_path)

# loop through all the files in the source folder and its subfolders
for root, dirs, files in os.walk(source_path):
    for file in files:
        # check if the file is an mp4 video file
        if file.endswith('.mp4'):
            # construct the full path to the file
            file_path = os.path.join(root, file)
            # construct the full path to the new folder, including the original subfolder name
            new_folder_path_with_subfolder = os.path.join(new_folder_path, os.path.relpath(root, source_path))
            # create the new subfolder if it doesn't already exist
            if not os.path.exists(new_folder_path_with_subfolder):
                os.mkdir(new_folder_path_with_subfolder)
            # construct the full path to the new file, including the new subfolder
            new_file_path = os.path.join(new_folder_path_with_subfolder, file)
            # move the file to the new folder
            if os.path.exists(new_file_path):
                os.remove(new_file_path)
            shutil.move(file_path, new_file_path)
