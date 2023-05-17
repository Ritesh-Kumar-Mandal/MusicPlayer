from tkinter import *
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
height = 300
## Set the position of the window
# x_position = 500
# y_position = 200
root.geometry(f"{width}x{height}")
# root.geometry(f"{width}x{height}+{x_position}+{y_position}")

## initialize the mixer to allow the music to be played
pygame.mixer.init()

## to run the App
root.mainloop()