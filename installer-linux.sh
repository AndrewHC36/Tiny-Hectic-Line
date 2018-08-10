#!/usr/bin/env bash
cd
echo "To stop the process, please press CTRL+C"
echo "And remember, run main.py in the folder"
echo "Input File Destitnation: "
read DIR
if [ ! -d "$DIR" ]; then
	echo "YOU MUST RESTART TO CONTINUE - DIRECTORY INVALID"
else
	cd $DIR
	mkdir TinyHecticLine
	cd TinyHecticLine
	git clone git://github.com/AndrewShen31/Tiny-Hectic-Line
	py main.py
fi
echo "PRESS ENTER TO EXIT"
read END
