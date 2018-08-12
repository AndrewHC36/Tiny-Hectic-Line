from src.constants import *
import pygame as pyg
pyg.init()


class Character:
    SCORE = 0  # Its like health point (hp)
    isDEAD = False
    stampPoint = []
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

    @classmethod
    def addStpPnt(cls, loc): cls.stampPoint.append(loc)

    @classmethod
    def addCurPnt(cls, loc): cls.stampPoint[-1] = loc

    def stamp(self, dir):
        for i in Character.stampPoint:
            if i != "BREAK": Character.stampPoint = [i[0], i[1]-dir[1]] # x dont chng bc char_pos x moves
        for i in range(len(Character.stampPoint)-1):  # -1 because its length, and suppose to use index
            if Character.stampPoint[i+1][0] == "BREAK": pass
            else: pyg.draw.line(self.WIN, STMP_COLOR, Character.stampPoint[i], Character.stampPoint[i+1], CHAR_SIZE//2)
        if len(Character.stampPoint) > 1:
            if Character.stampPoint[1][1] >= SCREEN[1]: del Character.stampPoint[0]

    @classmethod
    def die(cls): cls.isDEAD = True


class Tiles:

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

    def show(self, gen):
        for i in range(VIEW_BOX[0], VIEW_BOX[2]):
            for j in range(VIEW_BOX[1], VIEW_BOX[3]):
                if gen[j-VIEW_BOX[1]][i-VIEW_BOX[0]] != 0:
                    if gen[j-VIEW_BOX[1]][i-VIEW_BOX[0]] == 1: color = (100, 255, 0)
                    else: color = (gen[j-VIEW_BOX[1]][i-VIEW_BOX[0]]*2, 100, 0)
                    if j%2 == 0: x, y, X, Y = i*TILE_SIZE-self.bx, j//2*TILE_SIZE-self.by, i*TILE_SIZE+TILE_SIZE-self.bx, j//2*TILE_SIZE+TILE_SIZE-self.by
                    else: x, y, X, Y = i*TILE_SIZE-TILE_SIZE//2-self.bx, j//2*TILE_SIZE-TILE_SIZE//2-self.by, i*TILE_SIZE+TILE_SIZE//2-self.bx, j//2*TILE_SIZE+TILE_SIZE//2-self.by
                    pyg.draw.polygon(self.WIN, color, ((x+TILE_ORT, y), (X, y+TILE_ORT), (X-TILE_ORT, Y), (x, Y-TILE_ORT)))
                    #self.WIN.blit(pyg.font.SysFont('Arial', 30).render(str(gen[j-VIEW_BOX[1]][i-VIEW_BOX[0]]), False, (0, 0, 0)), (x+TILE_ORT, y+TILE_ORT))


class PointBox:
    high = 0
    current = 0

    def __init__(self, win, locA):  # <self>, <surface>, beginning location, end location
        self.WIN = win
        self.ax = locA[0]
        self.ay = locA[1]

    def show(self):
        self.WIN.blit(pyg.font.SysFont('Arial', 40).render(str("SCORE: "+str(PointBox.current)), False, (0, 0, 0)),(self.ax, self.ay))

    @classmethod
    def inc(cls, n): cls.current += n

    @classmethod
    def dnc(cls, n): cls.current -= n
