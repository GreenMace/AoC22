from aoccommon import *
import copy

with open('Dec5_input.txt') as f:
    lines = f.readlines()

    ins = False
    state = []
    moves = []
    for line in lines:
        if not line.strip():
            ins = True
            continue

        if ins:
            split = line.strip().split()
            moves.append([int(split[1]), int(split[3]) - 1, int(split[5]) - 1])
        elif line.strip().startswith("["):
            for i in range(1, len(line), 4):
                idx = int((i-1)/4)
                c = line[i]
                if not c == " ":
                    if idx < len(state):
                        state[idx].append(c)
                    else:
                        state.append([c])
                else:
                    if idx >= len(state):
                        state.append([])

    state1 = copy.deepcopy(state)
    state2 = copy.deepcopy(state)

    for move in moves:
        for i in range(move[0]):
            state1[move[2]].insert(0, state1[move[1]][0])
            state1[move[1]] = state1[move[1]][1:]

        max_move = min(move[0], len(state2[move[1]]))
        state2[move[2]] = state2[move[1]][0:max_move] + state2[move[2]]
        state2[move[1]] = state2[move[1]][max_move:]

    output1 = ""
    for c in state1:
        output1 += c[0]

    output2 = ""
    for c in state2:
        output2 += c[0]

    print("Part 1:", output1)
    print("Part 2:", output2)
