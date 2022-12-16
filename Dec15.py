from aoccommon import *

def dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def checkRow(S):
    for x in range(4000001):
        if not x % 100000:
            print(x)
        y = 0
        while y < 4000001:
            y_prev = y
            for s in S:
                d = s[2] - dist(s[0:2], [x,y])
                if d >= 0:
                    y += max(0, (s[1] - y)*2) + d + 1

            if y == y_prev:
                return (x,y)

with open('Dec15_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    y = 2000000
    S = []
    uniqueBatY = set()
    for line in lines:
        sl = line.split("=")
        x1 = int(sl[1].split(",")[0])
        y1 = int(sl[2].split(":")[0])
        x2 = int(sl[3].split(",")[0])
        y2 = int(sl[4])

        if y1 == y:
            uniqueBatY.add(x1)
        if y2 == y:
            uniqueBatY.add(x2)

        S.append([x1, y1, dist([x1, y1], [x2, y2])])

    r = set()
    for s in S:
        x = s[0]
        dx = (s[2] - abs(y - s[1]))
        r.update(list(range(x - dx, x + dx + 1)))

    beaconX, beaconY = checkRow(S)

    print("Part 1": len(r) - len(uniqueBatY))
    print(4000000 * beaconX + beaconY)
