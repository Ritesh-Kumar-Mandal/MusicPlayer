# Music Player using a Linked List

This is a Python program that implements a music player using a linked list data structure. The program allows you to load a folder of MP3 files, display them in a list, and play, pause, skip to the next or previous song. It provides a simple graphical user interface (GUI) using the [Tkinter](https://docs.python.org/3/library/tkinter.html) library.

## Installtion

```sh
git clone https://github.com/Ritesh-Kumar-Mandal/MusicPlayer.git
cd MusicPlayer
py -m pip install --upgrade pip
py -m pip install --user --upgrade virtualenv
py -m venv venv 
source venv/Scripts/activate 
pip3 install -r requirements.txt
py main.py
```

## Features

- Load a folder of MP3 files into the music player.
- Display the list of loaded songs in a graphical user interface.
- Play the selected song.
- Pause the currently playing song.
- Skip to the next or previous song in the playlist.

## Requirements

- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html) library
- [pygame](https://www.pygame.org/docs/ref/mixer.html) library
- [Pillow (PIL Fork)](https://pillow.readthedocs.io/en/stable/) library

## Installtion
```sh
git clone https://github.com/Ritesh-Kumar-Mandal/MusicPlayer.git
cd MusicPlayer
py -m pip install --upgrade pip
py -m pip install --user --upgrade virtualenv
py -m venv venv 
source venv/Scripts/activate 
pip3 install -r requirements.txt
```

## How to Use
1. Run the program:
```sh
py main.py
```
2. Click on "File" in the menu and select "Select Music Folder" to choose the folder containing your MP3 files.

3. The selected songs will be displayed in a list.

4. Click on a song in the list to play it.

5. Use the buttons at the bottom of the window to control the music player:
- Play button: Start playing the selected song.
- Pause button: Pause the currently playing song.
- Next button: Skip to the next song in the playlist.
- Previous button: Go back to the previous song in the playlist.

## Screenshots

![Main Window](https://github.com/Ritesh-Kumar-Mandal/MusicPlayer/blob/e841fdb3a240a48fd54555c5636c7af6d0b38be3/ScreenShots/MainWindow.png)

![File Menu](https://github.com/Ritesh-Kumar-Mandal/MusicPlayer/blob/e841fdb3a240a48fd54555c5636c7af6d0b38be3/ScreenShots/FileMenu.png)

![Add Music](https://github.com/Ritesh-Kumar-Mandal/MusicPlayer/blob/e841fdb3a240a48fd54555c5636c7af6d0b38be3/ScreenShots/Open%20Music%20Folder.png)

![Song List](https://github.com/Ritesh-Kumar-Mandal/MusicPlayer/blob/e841fdb3a240a48fd54555c5636c7af6d0b38be3/ScreenShots/SongList.png)

## Notes

- The program uses a linked list data structure to store the list of songs. Each song is represented by a node in the linked list.
- The program relies on the pygame library to play the MP3 files.
- The GUI is built using the Tkinter library, which provides standard GUI elements such as buttons and lists.
- The program dynamically loads the MP3 files from the selected folder, so you can easily update the song list by selecting a different folder.

Feel free to customize and enhance the program to fit your needs. Enjoy your music!

### Please star ✨ repository if you like it. Thank you!