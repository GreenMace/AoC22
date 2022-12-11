from aoccommon import *

def charToVal(c):
    value = ord(c)
    if value > 90:
        value -= 96
    else:
        value -= 38
    return value

with open('Dec3_input.txt') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]

    sum1 = 0
    sum2 = 0
    for i in range(0, len(lines), 3):
        for j in range(i, i+3):
            idx = int(len(lines[j])/2)
            sum1 += charToVal(strIntersect(lines[j][:idx], lines[j][idx:]))

        inboth = strIntersect(lines[i], lines[i+1])
        inboth = strIntersect(inboth, lines[i+2])

        sum2 += charToVal(inboth)

    print("Part 1:", sum1)
    print("Part 2:", sum2)
