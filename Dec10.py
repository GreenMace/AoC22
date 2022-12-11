from aoccommon import *

def render(cycle, position):
    output = "."
    if cycle % 40 in position:
        output = "#"

    if cycle in at2:
        output += "\n"

    return output

with open('Dec10_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    cycle = 1
    tot = 1
    at1 = list(range(20, 221, 40))
    at2 = list(range(40, 241, 40))
    vals = []
    output = ""
    for line in lines:
        pos = [(tot) % 40, (tot + 1) % 40, (tot + 2) % 40]
        output += render(cycle, pos)

        if cycle in at1:
            vals.append(tot*cycle)

        if not line.startswith("noop"):
            cycle += 1
            output += render(cycle, pos)

            if cycle in at1:
                vals.append(tot*cycle)
            tot += int(line.split()[1])

        cycle += 1

    print(sum(vals))
    print(output)
