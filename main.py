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

MAIN_CHAR = l.Character(WIN, CHAR_POS)
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

    MAIN_CHAR.show()
    MAIN_CHAR.stamp(DIR)
    MAIN_CHAR.update(CHAR_POS)
    #MAIN_CHAR.die()

    #pyg.draw.rect(WIN, (0,255,0), (CHAR_POS[0], CHAR_POS[1], TILE_SIZE, TILE_SIZE))
    #x, y, X, Y = CHAR_POS[0], CHAR_POS[1], CHAR_POS[0]+TILE_SIZE, CHAR_POS[1]+TILE_SIZE
    #pyg.draw.line(WIN, (0,255,0), (x//2, y), (X, y//2), 4)
    #pyg.draw.line(WIN, (0,255,0), (X, y), (X, Y), 4)
    #pyg.draw.line(WIN, (0,255,0), (X, Y), (x, Y), 4)
    #pyg.draw.line(WIN, (0,255,0), (x, Y), (x, y), 4)

    pyg.display.flip()
    CLK.tick(FPS)

pyg.quit()
quit()
