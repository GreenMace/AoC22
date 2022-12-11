from aoccommon import *

with open('Dec6_input.txt') as f:
    lines = f.readlines()

    o1 = 0
    o2 = 0
    for i in range(len(lines[0])):
        str1 = lines[0][i:i+4]
        str2 = lines[0][i:i+14]

        freq1 = countOcc(str1)
        if max(list(freq1.values())) == 1 and not o1:
            o1 = i+4

        freq2 = countOcc(str2)
        if max(list(freq2.values())) == 1 and not o2:
            o2 = i+14

    print("Task 1:", o1)
    print("Task 2:", o2)
