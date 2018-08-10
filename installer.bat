@echo off
cd C:\
echo "To stop the process, please press CTRL+C"
echo "And remember, run main.py in the folder"
set /p DEST="Input File Destitnation: "
if not exist "%DEST%" ( 
echo You must restart to continue because the directory is unvalid!
goto stop
)
cd "%DEST%"
md TinyHecticLine
cd TinyHecticLine
git clone git://github.com/AndrewShen31/Tiny-Hectic-Line
py main.py

goto end
:stop
set /p D="PRESS ENTER TO LEAVE"

:end