import sys

test_map=""".....
.S-7.
.|.|.
.L-J.
.....
"""

def parse_data(data):
    mp = data.splitlines()
    start = (-1, -1)
    for i in range(len(mp)):
        for j in range(len(mp[0])):
            if mp[i][j] == 'S':
                start = (i,j)
    return (mp, start)

def get_connected(start, mp):
    h = len(mp)
    w = len(mp[0])
    i, j = start
    pipe = mp[i][j]
    connected = []
    if pipe == '|':
        if i - 1 >= 0:
            connected.append((i-1,j))
        if i + 1 < h:
            connected.append((i+1,j))
    elif pipe == '-':
        if j - 1 >= 0:
            connected.append((i,j-1))
        if j + 1 < w:
            connected.append((i,j+1))
    elif pipe == 'L':
        if i - 1 >= 0:
            connected.append((i-1,j))
        if j + 1 < w:
            connected.append((i,j+1))
    elif pipe == 'J':
        if j - 1 >= 0:
            connected.append((i,j-1))
        if i - 1 >= 0:
            connected.append((i-1,j))
    elif pipe == '7':
        if i + 1 >= 0:
            connected.append((i+1,j))
        if j - 1 >= 0:
            connected.append((i,j-1))
    elif pipe == 'F':
        if i + 1 < h:
            connected.append((i+1,j))
        if j + 1 < w:
            connected.append((i,j+1))
    elif pipe == 'S':
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for oi, oj in offsets: 
            is_connected = False
            new_i = i+oi
            new_j = j+oj
            if (new_i >= 0 and new_j >= 0
                and new_i < h and new_j < w):
                    adj_pipe = mp[new_i][new_j]
                    if adj_pipe == '|':
                        if oi == -1 or oi == 1:
                            is_connected = True
                    elif adj_pipe == '-':
                        if oj == -1 or oj == 1:
                            is_connected = True
                    elif adj_pipe == 'L':
                        if oi == 1 or oj == -1:
                            is_connected = True
                    elif adj_pipe == 'J':
                        if oi == 1 or oj == +1:
                            is_connected = True
                    elif adj_pipe == '7':
                        if oi == -1 or oj == +1:
                            is_connected = True
                    elif adj_pipe == 'F':
                        if oi == -1 or oj == -1:
                            is_connected = True
                    if is_connected:
                        connected.append((new_i, new_j))
    return connected

def longest_path(mp, start, visited):
    pending = [start]
    while (len(pending) != 0):
        start = pending.pop(0)
        cnt = visited[start]+1
        conns = get_connected(start, mp)
        for con in conns:
            if con not in visited:
                visited[con]=cnt
                pending.append(con)
    return max(visited.values())

def solve(data):
    mp, start = parse_data(data)
    i, j = start
    visited = {start:0}
    steps = longest_path(mp, start, visited)
    return steps

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
