from aoccommon import *
import itertools

def mostPressure(map, rates, pos, to_open, dists, time = 26):
    if not to_open or time < 2:
        return 0

    dt = 0
    p = 0
    if pos in to_open:
        p = rates[pos] * (time - 1)
        to_open.remove(pos)
        dt = 1

    maxP = 0
    for dst in to_open:
        tt = dists[(pos, dst)] + dt
        p2 = p + mostPressure(map, rates, dst, to_open.copy(), dists, time - tt)
        maxP = max(maxP, p2)

    return maxP

def shortestPath(map, src, dst):
    neighbours = set(map[src])
    d = 1
    while True:
        for n in neighbours:
            if n == dst :
                return d

        neighbours = {n for neigh in neighbours for n in map[neigh]}
        d += 1

with open('Dec16_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    map = {}
    rates = {}
    for line in lines:
        sl = line.split(";")
        src = sl[0].split()[1]
        rate = int(sl[0].split("=")[-1])
        dst = []
        sl2 = sl[1].split()
        for i in range(4, len(sl2)):
            dst.append(sl2[i][0:2])

        map[src] = dst
        rates[src] = rate

    nonZero = set()
    for r in rates:
        if rates[r] > 0:
            nonZero.add(r)

    dist = {}
    for n in nonZero:
        dist[("AA", n)] = shortestPath(map, "AA", n)
        for nPrim in nonZero - set(n):
            dist[(n, nPrim)] = shortestPath(map, n, nPrim)

    print("Part 1:", mostPressure(map, rates, "AA", nonZero, dist, time = 30))
    tot = 0
    for i in range(1, int(len(nonZero)/2) + 1):
        EValves = list(itertools.combinations(list(nonZero), i))
        for j in range(len(EValves)):
            Et = mostPressure(map, rates, "AA", set(EValves[j]), dist)
            HValves = nonZero - set(EValves[j])
            Ht = mostPressure(map, rates, "AA", HValves, dist)
            tot = max(tot, Et + Ht)

    print("Part 2:", tot)
