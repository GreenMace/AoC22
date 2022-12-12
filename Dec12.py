from aoccommon import *

def shortestPath(map, starts, mapDist):
    queue = starts
    while queue:
        q = queue[0]

        neighbours = getNeighbours(map, q[0], q[1])
        for n in neighbours:
            if map[n[0]][n[1]] <= map[q[0]][q[1]] + 1:
                length = mapDist[toCoord(q)] + 1
                if toCoord(n) not in mapDist or length < mapDist[toCoord(n)]:
                    mapDist[toCoord(n)] = length
                    queue.append([n[0], n[1]])
        del queue[0]
    return mapDist

with open('Dec12_input.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

    map = []
    mapDist1 = {}
    mapDist2 = {}
    starts = []
    end = []
    for y in range(len(lines)):
        row = []
        for x in range(len(lines[y])):
            height = 0
            if lines[y][x] == "S":
                starts.insert(0, [y,x])

                mapDist1[toCoord([y,x])] = 0
                mapDist2[toCoord([y,x])] = 0
                height = ord("a") - ord("a")
            elif lines[y][x] == "E":
                end = [y,x]
                height = ord("z") - ord("a")
            else:
                height = ord(lines[y][x]) - ord("a")
                if not height:
                    mapDist2[toCoord([y,x])] = 0
                    starts.append([y,x])
            row.append(height)
        map.append(row)

    print("Part 1:", shortestPath(map, [starts[0]], mapDist1)[toCoord(end)])
    print("Part 2:", shortestPath(map, starts, mapDist2)[toCoord(end)])
