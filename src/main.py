"""
Author: Andrew Shen
Time: Aug 8, 2018
A game of 'Tiny Hectic Line'
"""

from src.constants import *
import pygame as pyg
from src import lib as l, gameGeneration as g
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
g.generate(GEN_TILES, (VIEW_BOX[2]-VIEW_BOX[0], VIEW_BOX[3]-VIEW_BOX[1]))
MAIN_CHAR.addStpPnt(CHAR_POS)
stp = False

while GAME_LOOP:
    WIN.fill(BACKG_COLOR)
    for e in pyg.event.get():
        if e.type == pyg.QUIT: GAME_LOOP = False
        elif e.type == pyg.KEYDOWN:
            if e.key == pyg.K_SPACE:
                if DIR == RIGHT: DIR = LEFT
                else: DIR = RIGHT
                MAIN_CHAR.addStpPnt(CHAR_POS)
            elif e.key == pyg.K_LSHIFT: stp = True
        elif e.type == pyg.KEYUP:
            if e.key == pyg.K_ESCAPE: GAME_LOOP = False
            elif e.key == pyg.K_LSHIFT: stp = False

    TILE.update(TERR_POS)
    TILE.show(GEN_TILES)

    MAIN_CHAR.addCurPnt(CHAR_POS)
    MAIN_CHAR.show()
    MAIN_CHAR.stamp(DIR)
    MAIN_CHAR.update(TERR_POS, CHAR_POS)

    if not stp:
        CHAR_POS[0] += DIR[0]
        TERR_POS[1] += DIR[1]

    if CHAR_POS[0] < -TILE_SIZE: CHAR_POS[0] = SCREEN[0]; MAIN_CHAR.addStpPnt(CHAR_POS)
    elif CHAR_POS[0] > SCREEN[0]: CHAR_POS[0] = -TILE_SIZE; MAIN_CHAR.addStpPnt(CHAR_POS)
    if TERR_POS[1] <= -TILE_SIZE:
        g.generateAdd(GEN_TILES)
        TERR_POS[1] += TILE_SIZE

    pyg.display.flip()
    CLK.tick(FPS)

pyg.quit()
quit()
