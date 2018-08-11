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

MAIN_CHAR = l.Character(WIN, TERR_POS, CHAR_POS)
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
    MAIN_CHAR.update(TERR_POS, CHAR_POS)

    CHAR_POS[0] += DIR[0]
    TERR_POS[1] += DIR[1]

    if CHAR_POS[0] < -TILE_SIZE: CHAR_POS[0] = SCREEN[0]
    elif CHAR_POS[0] > SCREEN[0]: CHAR_POS[0] = -TILE_SIZE

    if TERR_POS[1] <= -TILE_SIZE:
        TERR_POS[1] += TILE_SIZE

    pyg.display.flip()
    CLK.tick(FPS)

pyg.quit()
quit()
