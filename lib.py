from constants import *
import pygame as pyg
pyg.init()


class Character:
    SCORE = 0  # Its like health point (hp)
    isDEAD = False
    stampL = []

    def __init__(self, win, bloc, ploc):
        self.WIN = win
        self.px = ploc[0]
        self.py = ploc[1]
        self.bx = bloc[0]
        self.by = bloc[1]

    def update(self, bloc, ploc):
        self.px = ploc[0]
        self.py = ploc[1]
        self.bx = bloc[0]
        self.by = bloc[1]

    def show(self):
        if not Character.isDEAD: pyg.draw.circle(self.WIN, CHAR_COLOR, (self.px, self.py), CHAR_SIZE//2)

    def stamp(self, dir):
        Character.stampL.append([self.px, self.py])
        Character.stampL = [[i[0], i[1]-dir[1]] for i in Character.stampL]
        for i in Character.stampL:
            pyg.draw.rect(self.WIN, STMP_COLOR, (i[0]-CHAR_SIZE//4, i[1]-CHAR_SIZE//4, CHAR_SIZE//2, CHAR_SIZE//2))
        if Character.stampL[0][1] > SCREEN[1]+LOWER_BOUND_ADD: Character.stampL = Character.stampL[1:len(Character.stampL)]

    @classmethod
    def die(cls): cls.isDEAD = True


class Tiles:
    tile_data = []
    r = 0

    def __init__(self, win, bloc):
        self.WIN = win
        self.bx = bloc[0]
        self.by = bloc[1]

    def update(self, bloc):
        self.bx = bloc[0]
        self.by = bloc[1]

    @classmethod
    def generate(cls):
        pass

    def show(self):
        for i in range(VIEW_BOX[0], VIEW_BOX[2]):
            for j in range(VIEW_BOX[1], VIEW_BOX[3]):
                if j%2 == 0: x, y, X, Y = i*TILE_SIZE-self.bx, j//2*TILE_SIZE-self.by, i*TILE_SIZE+TILE_SIZE-self.bx, j//2*TILE_SIZE+TILE_SIZE-self.by
                else: x, y, X, Y = i*TILE_SIZE-TILE_SIZE//2-self.bx, j//2*TILE_SIZE-TILE_SIZE//2-self.by, i*TILE_SIZE+TILE_SIZE//2-self.bx, j//2*TILE_SIZE+TILE_SIZE//2-self.by
                pyg.draw.line(self.WIN, (0, 255, 0), (x+TILE_ORT, y), (X, y+TILE_ORT), 4)
                pyg.draw.line(self.WIN, (0, 255, 0), (X, y+TILE_ORT), (X-TILE_ORT, Y), 4)
                pyg.draw.line(self.WIN, (0, 255, 0), (X-TILE_ORT, Y), (x, Y-TILE_ORT), 4)
                pyg.draw.line(self.WIN, (0, 255, 0), (x, Y-TILE_ORT), (x+TILE_ORT, y), 4)



