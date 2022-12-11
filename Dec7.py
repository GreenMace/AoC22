from aoccommon import *

def reqDirSize(dir, key):
    size = 0
    for item in dir[key]:
        if type(item) == list:
            size += int(item[1])
        else:
            size += reqDirSize(dir, key + item + "/")

    return size

with open('Dec7_input.txt') as f:
    lines = f.readlines()

    paths = {"/": []}
    curr_path = [""]
    for line in lines:
        s = line.split()
        path_str = "/".join(curr_path) + "/"

        if s[0] == "$":
            if s[1] == "cd":
                if s[2] == "..":
                    del curr_path[-1]
                elif s[2] == "/":
                    curr_path = [""]
                else:
                    curr_path.append(s[2])
        elif s[0] == "dir":
            paths[path_str].append(s[1])
            paths[path_str + s[1] + "/"] = []
        else:
            paths[path_str].append([s[1], s[0]])

    sizes = {}
    for p in paths:
        addToDict(sizes, p, reqDirSize(paths, p))

    vals = list(sizes.values())

    bot = [x for x in vals if x <= 100000]

    needed = abs(40000000 - sizes["/"])
    top = [x for x in vals if x >= needed]
    top.sort()

    print(sum(bot))
    print(top[0])
