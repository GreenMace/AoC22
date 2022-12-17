from aoccommon import *
import copy
import time

leftEdge = 0
rightEdge = 6
bottom = 0

def moveRight(s, map):
    newShape = copy.deepcopy(s)
    for c in newShape:
        cx, cy = c
        if cx + 1 in map.get(cy, []) or cx == rightEdge:
            return s
        c[0] += 1


    return newShape

def moveLeft(s, map):
    newShape = copy.deepcopy(s)
    for c in newShape:
        cx, cy = c
        if cx - 1 in map.get(cy, []) or cx == leftEdge:
            return s
        c[0] -= 1

    return newShape

def moveDown(s, map):
    newShape = copy.deepcopy(s)
    for c in newShape:
        cx, cy = c
        if cx  in map.get(cy - 1, []) or cy == bottom:
            return (False, s)
        c[1] -= 1

    return (True, newShape)

def setStartHeight(s, height):
    for c in shape:
        c[1] += height + 3

with open('Dec17_input.txt') as f:
    lines = f.readlines()
    jets = lines[0].strip()

    shapes = [[[0,0],[1,0],[2,0],[3,0]],
            [[1,0],[0,1],[2,1],[1,2]],
            [[0,0],[1,0],[2,0],[2,1],[2,2]],
            [[0,0],[0,1],[0,2],[0,3]],
            [[0,0],[1,0],[0,1],[1,1]]]

    blocked = {}
    j = 0
    height = 0
    prev = 0
    sum = 0
    pattern = []
    for i in range(1000000):
        if i == 2022:
            print("Part 1:", height)
        shape = copy.deepcopy(shapes[i%5])
        setStartHeight(shape, height)
        shape = moveRight(shape, blocked)
        shape = moveRight(shape, blocked)

        falling = True
        while falling:
            dir = jets[j%len(jets)]
            if dir == "<":
                shape = moveLeft(shape, blocked)
            else:
                shape = moveRight(shape, blocked)

            (complete, shape) = moveDown(shape, blocked)
            if not complete:
                for c in shape:
                    height = max(height, c[1] + 1)
                    addToDict(blocked, c[1], c[0], True)
                falling = False

            j += 1

        if not (i+1) % 10000:
            pattern.append(height - prev)
            if len(pattern) > 2 and pattern[-1] == pattern[1]:
                sum = pattern[0] - pattern[-2]
                pattern[0] = pattern[-2]
                pattern = pattern[:-2]
                break
            prev = height

    print("Length: {}. Nice.".format(len(pattern)))
    for i in range(100000000):
        sum += pattern[i%len(pattern)]

    print("Part 2:", sum)
