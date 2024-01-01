import sys

def calc_nxt(curr, drs, grid):
    w=len(grid[0])
    h=len(grid)
    nxt = []
    for dr in drs:
        nxt_pos=None
        if dr=='l':
            nxt_pos = (curr[0], curr[1] - 1)
        elif dr=='r':
            nxt_pos = (curr[0], curr[1] + 1)
        elif dr=='u':
            nxt_pos = (curr[0] - 1, curr[1])
        elif dr=='d':
            nxt_pos = (curr[0] + 1, curr[1])
        if (nxt_pos[0] < h and nxt_pos[0] >= 0
            and nxt_pos[1] < w and nxt_pos[1] >= 0):
            nxt.append((nxt_pos, dr))
    return nxt

def current_dirs(curr, prev_dr, grid):
    tile = grid[curr[0]][curr[1]]
    if tile == '.':
        return [prev_dr]
    elif tile == '/' or tile == '\\':
        nxt_dr = None
        if tile == '/' and prev_dr == 'l':
            nxt_dr = 'd'
        elif tile == '/' and prev_dr == 'r':
            nxt_dr = 'u'
        elif tile == '/' and prev_dr == 'd':
            nxt_dr = 'l'
        elif tile == '/' and prev_dr == 'u':
            nxt_dr = 'r'
        elif tile == '\\' and prev_dr == 'l':
            nxt_dr = 'u'
        elif tile == '\\' and prev_dr == 'r':
            nxt_dr = 'd'
        elif tile == '\\' and prev_dr == 'd':
            nxt_dr = 'r'
        elif tile == '\\' and prev_dr == 'u':
            nxt_dr = 'l'
        return [nxt_dr]
    elif tile == '-' or tile == '|':
        if (tile == '-' and (prev_dr == 'u' or prev_dr == 'd')):
            return ['l', 'r']
        elif (tile == '-' and (prev_dr == 'l' or prev_dr == 'r')):
            return [prev_dr]
        elif (tile == '|' and (prev_dr == 'l' or prev_dr == 'r')):
            return ['d', 'u']
        elif (tile == '|' and (prev_dr == 'u' or prev_dr == 'd')):
            return [prev_dr]
    return []

def fill_tiles(energized, grid, curr, prev_dr):
    drs = current_dirs(curr, prev_dr, grid)
    tmp_drs= list(drs)
    if curr not in energized:
        energized[curr] = drs
    else:
        tmp_drs.clear()
        stop = True
        for dr in drs:
            if dr not in energized[curr]:
                tmp_drs.append(dr)
                energized[curr].append(dr)
                stop=False
        if stop:
            return
    for nxt, dr in calc_nxt(curr, tmp_drs, grid):
        fill_tiles(energized, grid, nxt, dr)

def solve(data):
    grid = data.splitlines()
    energized = {}
    fill_tiles(energized, grid, (0,0), 'r')
    '''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i,j) in energized:
                print('#',end='')
            else:
                print('.', end='')
        print()
    '''
    return len(energized)

def main(*args):
    sys.setrecursionlimit(10000000)
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
