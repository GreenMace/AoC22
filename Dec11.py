from aoccommon import *

def updateValue(old, op):
    return eval(op)

with open('Dec11_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    inspected1 = [0 for i in range(int(len(lines)/7)+1)]
    inspected2 = [0 for i in range(int(len(lines)/7)+1)]

    mPos1 = {}
    mPos2 = {}
    mChar = {}
    totDivide = 1
    for i in range(0, len(lines), 7):
        monkey = int(i / 7)
        items = lines[i+1].split(":")[1]
        items = [int(x.strip()) for x in items.split(",")]
        addToDict(mPos1, monkey, items.copy())
        addToDict(mPos2, monkey, items.copy())

        op = lines[i+2].split("=")[-1]
        test = int(lines[i+3].split()[-1])
        true = int(lines[i+4].split()[-1])
        false = int(lines[i+5].split()[-1])
        addToDict(mChar, monkey, [op, test, true, false])

        totDivide *= test

    for i in range(20):
        for m in mChar:
            inspected1[m] += len(mPos1[m])
            for y in mPos1[m]:
                y = updateValue(y, mChar[m][0])
                y /= 3

                if y % mChar[m][1]:
                    mPos1[mChar[m][3]].append(y)
                else:
                    mPos1[mChar[m][2]].append(y)

            mPos1[m] = []

    for i in range(10000):
        for m in mChar:
            inspected2[m] += len(mPos2[m])
            for y in mPos2[m]:
                y = updateValue(y, mChar[m][0])
                y = y % totDivide

                if y % mChar[m][1]:
                    mPos2[mChar[m][3]].append(y)
                else:
                    mPos2[mChar[m][2]].append(y)

            mPos2[m] = []

    inspected1.sort()
    inspected2.sort()
    print("Part 1:", inspected1[-1]*inspected1[-2])
    print("Part 2:", inspected2[-1]*inspected2[-2])
