from tkinter import *
from tkinter import filedialog
import pygame
import os

root = Tk()
root.title("Music Player")
root.geometry("500x400")

# Define colors
bg_color = "#F7EDE2"  # beige
text_color = "#2F4858"  # dark greenish-blue
button_color = "#5C748E"  # light bluish-gray
highlight_color = "#CAD2C5"  # light grayish-green

# Set background color
root.configure(bg=bg_color)

# Define the song list and current song index variables
songs = []
current_song = 0

# Initialize Pygame mixer
pygame.mixer.init()

# Define function to load the selected song
def load_song():
    global current_song
    selection = listbox.curselection()
    if len(selection) > 0:
        stop_song()
        current_song = selection[0]
        song = songs[current_song]
        label.config(text=song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

# Define function to stop the currently playing song
def stop_song():
    pygame.mixer.music.stop()

# Define function to pause and resume the currently playing song
def pause_resume_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

# Define function to set the volume of the music player
def set_volume(val):
    volume = float(val) / 100.0
    pygame.mixer.music.set_volume(volume)

# Define function to select folder containing songs
def select_folder():
    global songs
    folder_path = filedialog.askdirectory()
    if folder_path:
        songs = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3") or filename.endswith(".wav"):
                songs.append(os.path.join(folder_path, filename))
        listbox.delete(0, END)
        for song in songs:
            listbox.insert(END, os.path.basename(song))
    
# Create the user interface
frame1 = Frame(root, bg=bg_color)
frame1.pack(side=TOP, padx=20, pady=20)

label = Label(frame1, text="Select a song to play", font=("Arial", 14), fg=text_color, bg=bg_color)
label.pack(side=LEFT)

frame2 = Frame(root, bg=bg_color)
frame2.pack(side=TOP, padx=20, pady=20)

listbox = Listbox(frame2, width=50, height=20, bg=button_color, fg=text_color, selectbackground=highlight_color, selectforeground=text_color)
listbox.pack(side=LEFT)

scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

frame3 = Frame(root, bg=bg_color)
frame3.pack(side=TOP, padx=20, pady=20)

load_button = Button(frame3, text="Load Song", command=load_song, bg=button_color, fg=text_color, highlightbackground=highlight_color)
load_button.pack(side=LEFT, padx=10)

pause_resume_button = Button(frame3, text="Pause/Resume", command=pause_resume_song, bg=button_color, fg=text_color, highlightbackground=highlight_color)
pause_resume_button.pack(side=LEFT, padx=10)

stop_button = Button(frame3, text="Stop", command=stop_song)
stop_button.pack(side=LEFT, padx=10)

volume_scale = Scale(frame3, from_=0, to=100, orient=HORIZONTAL, command=set_volume)
volume_scale.set(50)
volume_scale.pack(side=LEFT, padx=10)

select_folder_button = Button(frame3, text="Select Folder", command=select_folder)
select_folder_button.pack(side=LEFT, padx=10)

# Set initial state of variables
paused = False

# Start the Tkinter event loop
root.mainloop()
