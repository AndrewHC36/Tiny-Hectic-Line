"""
Author: Andrew Shen
Time: Aug 8, 2018
A game of 'Tiny Hectic Line'
"""

from constants import *
import pygame as pyg
import lib as l
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

pyg.init()
WIN = pyg.display.set_mode((0, 0), pyg.FULLSCREEN)
CLK = pyg.time.Clock()

GAME_LOOP = True
DIR = RIGHT
CHAR_POS = STARTING_POS  # character pos
TERR_POS = [0, 0]
OFFSET = [0, 0]

MAIN_CHAR = l.Character(WIN, CHAR_POS)
TILE = l.Tiles(WIN, TERR_POS)
GEN_TILES = []

while GAME_LOOP:
    WIN.fill(BACKG_COLOR)
    for e in pyg.event.get():
        if e.type == pyg.QUIT: GAME_LOOP = False
        elif e.type == pyg.KEYDOWN:
            if e.key == pyg.K_SPACE:
                if DIR == RIGHT: DIR = LEFT
                else: DIR = RIGHT
        elif e.type == pyg.KEYUP:
            if e.key == pyg.K_ESCAPE: GAME_LOOP = False

    TILE.update(TERR_POS)
    TILE.show()

    MAIN_CHAR.show()
    MAIN_CHAR.stamp(DIR)
    MAIN_CHAR.update(CHAR_POS)

    TERR_POS[0] += DIR[0]
    TERR_POS[1] += DIR[1]

    pyg.display.flip()
    CLK.tick(FPS)

pyg.quit()
quit()
