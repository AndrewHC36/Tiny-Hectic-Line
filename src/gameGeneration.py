import random as r
from src.constants import *

gameGen = []

def generate(dt, size):
    for i in range(size[1]):  # y
        dt.append([])
        for j in range(size[0]):  # x
            if j == STARTING_POS[0]//TILE_SIZE: dt[i].append(1)
            else: dt[i].append(0)

def generateAdd(dt):
    for j in range(2):
        cur, last = [], dt[j]
        for i in range(len(dt[0])):
            n = r.randint(0, 1)
            if last[i-1] != 0 and n == 0: cur.append(r.randint(1, 100))
            elif last[i] != 0 and n == 1: cur.append(r.randint(1, 100))
            else: cur.append(0)
        dt.insert(0, cur)
    del dt[-2:]
