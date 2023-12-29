import sys

def count_rocks(lines):
    h = len(lines)
    w = len(lines[0])
    count=0
    for i in range(h):
        value = h - i
        for j in range(w):
            if lines[i][j] == 'O':
                count+=value
    return count

def make_grid(data):
    grid=data.splitlines()
    grid = [[c for c in line] for line in grid]
    return grid

def tilt_north(grid, w, h):
    last = [0 for _ in range(w)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                grid[last[j]][j]='O'
                last[j]+=1
            elif grid[i][j] == '#':
                last[j] = i+1

def tilt_west(grid, w, h):
    last = [0 for _ in range(h)]
    for j in range(w):
        for i in range(h):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                grid[i][last[i]]='O'
                last[i]+=1
            elif grid[i][j] == '#':
                last[i] = j+1

def tilt_south(grid, w, h):
    last = [h-1 for _ in range(w)]
    for i in range(h-1, -1, -1):
        for j in range(w):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                grid[last[j]][j]='O'
                last[j]-=1
            elif grid[i][j] == '#':
                last[j] = i-1

def tilt_east(grid, w, h):
    last = [w-1 for _ in range(h)]
    for j in range(w-1, -1, -1):
        for i in range(h):
            if grid[i][j] == 'O':
                grid[i][j] = '.'
                grid[i][last[i]]='O'
                last[i]-=1
            elif grid[i][j] == '#':
                last[i] = j-1

def do_cycle(grid, w, h):
    tilt_north(grid, w, h)
    tilt_west(grid, w, h)
    tilt_south(grid, w, h)
    tilt_east(grid, w, h)

def convert_2_str(grid):
    string=''
    for line in grid:
        line = ''.join(line)
        string+=line+'\n'
    return string

def find_cycle(grid, w, h):
    i=0
    first=None
    tmp=grid
    cycle=0
    cycles={}
    while True:
        do_cycle(tmp, w, h)
        cycle+=1
        string = convert_2_str(tmp)
        if string in cycles:
            return (cycles[string], cycle - cycles[string])
        else:
            cycles[string]=cycle

def solve(data):
    tmp=make_grid(data)
    w=len(tmp[0])
    h=len(tmp)
    first, cycle_cnt = find_cycle(tmp, w, h)
    iters=1000000000
    iters-=first
    iters %= cycle_cnt
    for _ in range(iters):
        do_cycle(tmp, w, h)

    return count_rocks(tmp)

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
