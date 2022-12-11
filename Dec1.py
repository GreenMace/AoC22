from aoccommon import *

with open('Dec1_input.txt') as f:
    lines = f.readlines()

    top3 = [0, 0, 0]
    current = 0
    for line in lines:
        if line == "\n":
            if current > top3[0]:
                top3[0] = current
                top3.sort()
            current = 0
        else:
            current += int(line)


    print("Part 1:", top3[-1])
    print("Part 2:", sum(top3))
