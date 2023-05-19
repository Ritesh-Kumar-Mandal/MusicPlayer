from LinkedList import LinkedList
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import logging

## To Hide Pygame 
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


## Initialize the App & create a GUI window
root = Tk()
## Set title of the Window
root.title("Music Player")

## Set the size of your window 
width = 500
height = 320 
## Set the position of the window
# x_position = 500
# y_position = 200
root.geometry(f"{width}x{height}")
# root.geometry(f"{width}x{height}+{x_position}+{y_position}")

## initialize the mixer to allow the music to be played
pygame.mixer.init()

## Add a menu bar to the root window
menu_bar = Menu(root)
root.config(menu=menu_bar)      ## To set the root's menu bar to our menu bar

##---------------------------------------------------------------------------------------------------------------

songs = LinkedList()            ## Using the Created LinkedList DataStructure to store the songs list
current_song = ""
paused = False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)

        if ext == '.mp3':
            songs.append(song)
    
    for i in range(songs.length()):
        song_list.insert("end", songs.get(i))
    
    song_list.select_set(0)
    current_song = songs.get(song_list.curselection()[0])       ## To make the current song which selected in the song list

def play_music():
    global current_song, paused

    ## To get current selected song in-case user want to play different song while listening to other song
    current_song = songs.get(song_list.curselection()[0])

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))  ## path.join will join the chosen directory path and the song name
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    
    global paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next_music():
    global current_song, paused

    try:
        song_list.selection_clear(0, END)  
        song_list.select_set(songs.index(current_song) + 1)
        current_song = songs.get(song_list.curselection()[0])           
        play_music()
    except Exception as e:

        pass ## Do nothing when we receive when we are at the end of the list user hits next song

def prev_music():
    global current_song, paused

    try:
        song_list.selection_clear(0, END)
        song_list.select_set(songs.index(current_song) - 1)
        current_song = songs.get(song_list.curselection()[0])
        play_music()
    except Exception as e:
        pass ## Do nothing when we receive when we are at the start of the list user hits prev song


##---------------------------------------------------------------------------------------------------------------

organise_menu = Menu(menu_bar, tearoff=False)               ## Creating a organised menu     # tearoff=False, will remove default row created in menu
organise_menu.add_command(label='Select Music Folder', command=load_music)      ## Adding a command to our organised menu
menu_bar.add_cascade(label='File', menu=organise_menu)      ## Adding our organised menu to root's menu

song_list = Listbox(root, bg="black", fg="white", width=100, height=15)
song_list.pack() ## 'pack' adds your widget to the root window

## Import the button images
play_btn_image = ImageTk.PhotoImage(Image.open("icons/play-button.png").resize((48, 48))) ## Read the Image using Image.open() ## Resize the image using resize((width, height)) method
pause_btn_image = ImageTk.PhotoImage(Image.open("icons/pause-button.png").resize((48, 48)))
next_btn_image = ImageTk.PhotoImage(Image.open("icons/next-button.png").resize((48, 48)))
previous_btn_image = ImageTk.PhotoImage(Image.open("icons/previous-button.png").resize((48, 48)))

control_frame = Frame(root)         ## Its like section in your window in which you can add and organize your widgets, just like 'div' in HTML
control_frame.pack()

play_btn = Button(control_frame, image= play_btn_image, borderwidth=0, command=play_music)          #borderwidth=0 to keep no space between the buttons
pause_btn = Button(control_frame, image= pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image= next_btn_image, borderwidth=0, command=next_music)
previous_btn = Button(control_frame, image= previous_btn_image, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)         ## Using grid instead of pack to organise the widgets in the frame
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=0, padx=7, pady=10)

## to run the App
root.mainloop()