from aoccommon import *

def cmpLst(left, right):
    for i in range(len(left)):
        if i == len(right):
            return False

        if type(left[i]) == list or type(right[i]) == list:
            l = left[i] if isinstance(left[i], list) else [left[i]]
            r = right[i] if isinstance(right[i], list) else [right[i]]
            cmp = cmpLst(l, r)
            if cmp:
                return True
            elif cmp is not None:
                return False
        elif not left[i] == right[i]:
            return left[i] < right[i]

    if len(left) < len(right):
        return True
    return None

with open('Dec13_input.txt') as f:
    lines = f.readlines()
    lines = [eval(line.strip()) for line in lines if not line == "\n"]

    pos2 = 1
    pos6 = 2
    sum = 0
    for i in range(0,len(lines),2):
        if not cmpLst(lines[i], lines[i+1]) == False:
            sum += int(i/2 + 1)

        pos2 += int(not cmpLst(lines[i], [[2]]) == False)
        pos2 += int(not cmpLst(lines[i+1], [[2]]) == False)
        pos6 += int(not cmpLst(lines[i], [[6]]) == False)
        pos6 += int(not cmpLst(lines[i+1], [[6]]) == False)

    print("Part 1:", sum)
    print("Part 2:", pos2 * pos6)
