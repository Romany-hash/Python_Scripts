import os
import time
import ctypes

# Define the path to the USB drive
usb_path = "D:\\"

# Wait for the USB drive to be inserted
while not os.path.exists(usb_path):
    time.sleep(1)

# Check for autorun.inf file on the USB drive
autorun_path = os.path.join(usb_path, "autorun.inf")
if os.path.exists(autorun_path):
    # Delete the autorun.inf file
    os.remove(autorun_path)
    
    # Display a message on the screen
    ctypes.windll.user32.MessageBoxW(0, "This is a hacker!", "Warning", 0x10)
