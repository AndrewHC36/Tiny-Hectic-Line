import random as r

gameGen = []

def generate(dt, size):
    for i in range(size[1]):  # y
        dt.append([])
        for j in range(size[0]):  # x
            dt[i].append(r.randint(0,1))

def generateAdd(dt):
    for j in range(2):
        cur = []
        for i in range(len(dt[0])):
            if i == 5: cur.append(1)
            else: cur.append(1)
        dt.insert(0, cur)
    del dt[-2:]

