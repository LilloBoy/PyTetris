# PyTetris

Simply the Game of Tetris written in python. This will be the starting point for a bigger project where the game will be playable on a wall mounted array of LEDs beeing executed
on a raspberry pi zero.

The code is divided in two files: main.py beeing the graphical part of the code where, in this stage of the project, the games window's handled but in the future i will handle the
array of LEDs and a second file Tetris.py beeing the actual game, where all the calculation, collison detections and pieces movement is handled.
The code is structured in such way to ease up the conversion from graphical to LED display because at the moment i'm unable to test it on the final setup. With this approach i'll
only need to change a couple of lines of code in the main.py file to completelly convert it.
