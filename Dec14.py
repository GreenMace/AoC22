from aoccommon import *

def sandRests(map, mapMax, x = 500, y = 0, floor = False):
    if y in map.get(x, []):
        return False

    while y + 1 < mapMax:
        y += 1
        if y not in map.get(x, []):
            pass
        elif y not in map.get(x-1, []):
            x -= 1
        elif y not in map.get(x+1, []):
            x += 1
        else:
            y -= 1
            break
    else:
        if not floor:
            return False

    addToDict(map, x, y, append = True)
    return True

with open('Dec14_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    walls = {}
    for line in lines:
        corners = [eval("[" + x + "]") for x in line.split(" -> ")]

        for i in range(len(corners)-1):
            (x1, y1), (x2, y2) = corners[i], corners[i+1]
            if x1 == x2:
                dy = -1 + 2*(y1 < y2)
                for y in range(y1, y2 + dy, dy):
                    addToDict(walls, x1, y, append = True)
            else:
                dx = -1 + 2*(x1 < x2)
                for x in range(x1, x2 + dx, dx):
                    addToDict(walls, x, y1, append = True)

    mapMax = max([x for y in walls.values() for x in y]) + 1

    resting = 0
    while sandRests(walls, mapMax, floor = False):
        resting += 1
    print("Part 1:", resting)
    mapMax += 1
    while sandRests(walls, mapMax, floor = True):
        resting += 1

    print("Part 2:", resting)
