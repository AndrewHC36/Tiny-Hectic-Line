from constants import *
import pygame as pyg
pyg.init()


class Character:
    SCORE = 0  # Its like health point (hp)
    isDEAD = False
    stampL = []

    def __init__(self, win, ploc):
        self.WIN = win
        self.px = ploc[0]
        self.py = ploc[1]

    def update(self, ploc):
        self.px = ploc[0]
        self.py = ploc[1]

    def show(self):
        if not Character.isDEAD: pyg.draw.circle(self.WIN, CHAR_COLOR, (self.px, self.py), CHAR_SIZE//2)

    def stamp(self, dir):
        Character.stampL.append([self.px, self.py])
        Character.stampL = [[i[0]-dir[0], i[1]-dir[1]] for i in Character.stampL]
        for i in Character.stampL:
            pyg.draw.rect(self.WIN, STMP_COLOR, (i[0]-CHAR_SIZE//4, i[1]-CHAR_SIZE//4, CHAR_SIZE//2, CHAR_SIZE//2))
        if Character.stampL[0][1] > SCREEN[1]+LOWER_BOUND_ADD: Character.stampL = Character.stampL[1:len(Character.stampL)]

    @classmethod
    def die(cls): cls.isDEAD = True


def generateTile():
    sdt = []

    return sdt
