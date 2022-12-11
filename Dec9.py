from aoccommon import *

def followY(head, section):
    if section[1] < head[1]:
        section[1] += 1
    elif section[1] > head[1]:
        section[1] -= 1

def followX(head, section):
    if section[0] < head[0]:
        section[0] += 1
    elif section[0] > head[0]:
        section[0] -= 1

def moveSection(head, section):
    if section[0] < head[0] - 1:
        followY(head, section)
        section[0] += 1
    elif section[0] > head[0] + 1:
        followY(head, section)
        section[0] -= 1
    elif section[1] > head[1] + 1:
        followX(head, section)
        section[1] -= 1
    elif section[1] < head[1] - 1:
        followX(head, section)
        section[1] += 1

with open('Dec9_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    hPos = [0,0]
    tPos = [[0,0] for i in range(9)]
    visited1 = [[0,0]]
    visited2 = [[0,0]]
    for line in lines:
        sLine = line.split()
        for i in range(int(sLine[1])):
            if sLine[0] == "L":
                hPos[0] -= 1
            elif sLine[0] == "D":
                hPos[1] -= 1
            elif sLine[0] == "U":
                hPos[1] += 1
            else:
                hPos[0] += 1

            moveSection(hPos, tPos[0])
            for t in range(1, len(tPos)):
                moveSection(tPos[t-1], tPos[t])

            if tPos[0] not in visited1:
                visited1.append(tPos[0].copy())
            if tPos[-1] not in visited2:
                visited2.append(tPos[-1].copy())

    print(len(visited1))
    print(len(visited2))
