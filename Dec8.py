from aoccommon import *

def checkDir(map, y, x, dy, dx, orig, count = 1):
    if x > 0 and x < len(map[y]) - 1 and y > 0 and y < len(map) - 1:
        if map[y + dy][x + dx] < orig:
            return checkDir(map, y + dy, x + dx, dy, dx, orig, count + 1)
        return (count, False)
    else:
        return (count - 1, True)

with open('Dec8_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = toMap(lines)

    maximum = 0
    vis = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            (up, v1) = checkDir(lines, i, j, -1, 0, lines[i][j])
            (down, v2) = checkDir(lines, i, j, 1, 0, lines[i][j])
            (left, v3) = checkDir(lines, i, j, 0, -1, lines[i][j])
            (right, v4) = checkDir(lines, i, j, 0, 1, lines[i][j])

            if (v1 or v2 or v3 or v4):
                vis += 1

            tot = up*down*right*left
            maximum = max(maximum, tot)

    print(vis)
    print(maximum)
