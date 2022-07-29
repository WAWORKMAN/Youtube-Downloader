from linecache import getline
from tkinter import * 
from tkinter import filedialog
from moviepy import * 
from moviepy.video.io.VideoFileClip import VideoFileClip

# THESE IMPORTS MAKE THE EXE FILE WORK
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from pytube import YouTube


# Allows the user to select a path from File Explorer
def select_path(*args):
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file(*args):
    # Gets user path
    get_link = link_field.get()

    # Gets selected path
    user_path = path_label.cget("text")

    # Downloads video and will get the highest resolution possible
    video = YouTube(get_link).streams.get_highest_resolution().download()
    clip = VideoFileClip(video)
    clip.close()




# Rest of the code sets up the Tkinter window
root = Tk()


# Window size and title
title = root.title("Youtube Video Downloader")
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()


# Field to enter link. Canvas adds field to window
link_field = Entry(root, width = 50)
canvas.create_window(250, 220, window=link_field)


# Text label above entry field. Canvas adds label to window
link_label = Label(root, text="Enter Download Link: ", font="Arial, 16")
canvas.create_window(250, 170, window=link_label)


# Path for saved Youtube video
path_label = Label(root, text="Select Path For Download", font="Arial, 16")
select_button = Button(root, text="Select", command=select_path)
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_button)


# Download button
download_button = Button(root, text="Download File", command=download_file)
canvas.create_window(250, 390, window=download_button)


# Window loop
root.mainloop()
