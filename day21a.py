import sys
from collections import deque

def find_s(mp):
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if mp[i][j] == "S":
                return (j, i)
    return None

def is_access(x, y, mp):
    w = len(mp[0])
    h = len(mp)
    if x < 0 or x >= w or y < 0 or y>=h:
        return False
    return mp[y][x] == "." or mp[y][x] == "S"

def solve(data):
    mp = data.splitlines()
    init_pos = find_s(mp)
    visited = set([init_pos])
    cnt = 0
    while True:
        if cnt == 64:
            break
        v_aux = set()
        for pos in visited:
            if is_access(pos[0]+1, pos[1], mp):
                v_aux.add((pos[0]+1, pos[1]))
            if is_access(pos[0]-1, pos[1], mp):
                v_aux.add((pos[0]-1, pos[1]))
            if is_access(pos[0], pos[1]+1, mp):
                v_aux.add((pos[0], pos[1] + 1))
            if is_access(pos[0], pos[1]-1, mp):
                v_aux.add((pos[0], pos[1] - 1))
        visited.clear()
        visited.update(v_aux)
        cnt += 1
    return len(visited)


def print_mat(visited, mp):
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if (j,i) in visited:
                print('O', end="")
            else:
                print(mp[i][j], end="" )
        print("")

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
