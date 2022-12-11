from aoccommon import *

def calcPoints(x, y):
    if x == y:
        return x + 3
    elif x == o + 1 or x == y - 2:
        return x + 6
    else:
        return x

with open('Dec2_input.txt') as f:
    lines = f.readlines()

    points1 = 0
    points2 = 0
    for line in lines:
        sl = line.split()

        op = {"A": 1, "B": 2, "C": 3}

        pp = {"X": 1, "Y": 2, "Z": 3}
        o = op[sl[0]]
        p1 = pp[sl[1]]

        p2 = o
        if sl[1] == "X":
            p2 = o - 1
        elif sl[1] == "Z":
            p2 = o + 1

        if p2 > 3:
            p2 = 1
        if p2 < 1:
            p2 = 3

        points1 += calcPoints(p1, o)
        points2 += calcPoints(p2, o)

    print("Part 1:", points1)
    print("Part 2:", points2)
