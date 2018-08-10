#!/usr/bin/env bash
mkdir TinyHecticLine
cd TinyHecticLine
git clone git://github.com/AndrewShen31/Tiny-Hectic-Line
cd Tiny-Hectic-Line
rm -f installer-win.bat
rm -r -f .git
rm -r -f .idea
rm -r -f __pycache__
clear
echo Remember, run main.py in the folder
echo To exit the game, press [ESC] button
echo PRESS ENTER TO PLAY Tiny-Hectic-Line
read END
py main.py