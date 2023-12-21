import sys

def get_galaxies(data):
    galaxies = []
    for i, line in enumerate(data.splitlines()):
        for j, c in enumerate(line):
            if c == '#':
                galaxies.append((i,j))
    return galaxies

def get_empty(data):
    rows=set()
    for i, line in enumerate(data.splitlines()):
        empty=True
        for j, c in enumerate(line):
            if c != '.':
                empty=False
                break
        if empty:
            rows.add(i)

    cols=set()
    lines= data.splitlines()
    for j in range(len(lines[0])):
        empty=True
        for i in range(len(lines)):
            if lines[i][j] != '.':
                empty=False
                break
        if empty:
            cols.add(j)

    return (rows, cols)

def get_combinations(gxs):
    cmbs=[]
    for i in range(len(gxs)):
        j=i+1
        while j < len(gxs):
            cmbs.append((gxs[i],gxs[j]))
            j+=1
    return cmbs

def sum_distances(gxs, rows, cols):
    total=0
    for (ga_y, ga_x), (gb_y,gb_x) in gxs:
        dist=0
        if ga_x < gb_x:
            dif = gb_x - ga_x
            for i in range(ga_x+1, gb_x):
                if i in cols:
                    dif+=1
            dist+=dif
        else:
            dif = ga_x - gb_x
            for i in range(gb_x+1, ga_x):
                if i in cols:
                    dif+=1
            dist+=dif
        if ga_y < gb_y:
            dif = gb_y - ga_y
            for i in range(ga_y+1, gb_y):
                if i in rows:
                    dif+=1
            dist+=dif
        else:
            dif = ga_y - gb_y
            for i in range(gb_y+1, ga_y):
                if i in rows:
                    dif+=1
            dist+=dif
        total+=dist
    return total


def solve(data):
    gxs = get_galaxies(data)
    gxs = get_combinations(gxs)
    rows, cols = get_empty(data)
    return sum_distances(gxs, rows, cols)

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
