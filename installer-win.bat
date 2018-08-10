@echo off
md TinyHecticLine
cd TinyHecticLine
git clone git://github.com/AndrewShen31/Tiny-Hectic-Line
cd Tiny-Hectic-Line
del installer-linux.sh
rmdir /S /Q .git
rmdir /S /Q .idea
rmdir /S /Q __pycache__
cls
echo Remember, run main.py in the folder
echo To exit the game, press [ESC] button
set /p END="PRESS ENTER TO PLAY Tiny-Hectic-Line"
py main.py