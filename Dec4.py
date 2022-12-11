from aoccommon import *

with open('Dec4_input.txt') as f:
    lines = f.readlines()
    lines = [l.strip().split(",") for l in lines]

    pairs1 = 0
    pairs2 = 0
    for line in lines:
        p1 = intList(line[0].split("-"))
        p2 = intList(line[1].split("-"))

        pairs1 += contained(p1[0], p1[1], p2[0], p2[1], full = True)
        pairs2 += contained(p1[0], p1[1], p2[0], p2[1], full = False)

    print("Part 1:", pairs1)
    print("Part 2:", pairs2)
