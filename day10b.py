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
        if i - 1 >= 0:
            connected.append((i-1,j))
        if j - 1 >= 0:
            connected.append((i,j-1))
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
        offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]
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

def find_loop(mp, start):
    pending = [start]
    visited = {start:False}
    while (len(pending) != 0):
        start = pending.pop(0)
        cnt = visited[start]+1
        conns = get_connected(start, mp)

        #Check if vertical wall
        if (conns[0][0] != start[0] and
            conns[1][0] != start[0]):
            visited[start]=True
        #Check if corner pointing upwards
        elif (conns[0][0] < conns[1][0]
              and conns[0][1] < conns[1][1]):
            if start[0] - 1 == conns[0][0]:
                visited[start]=True
        elif (conns[0][0] < conns[1][0]
              and conns[0][1] > conns[1][1]):
            if start[0] - 1 == conns[0][0]:
                visited[start]=True
        elif (conns[0][0] > conns[1][0]
              and conns[0][1] > conns[1][1]):
            if start[0] - 1 == conns[1][0]:
                visited[start]=True
        elif (conns[0][0] > conns[1][0]
              and conns[0][1] < conns[1][1]):
            if start[0] - 1 == conns[1][0]:
                visited[start]=True

        for con in conns:
            if con not in visited:
                visited[con]=False
                pending.append(con)
    return visited

def solve(data):
    mp, start = parse_data(data)
    loop = find_loop(mp, start)
    cnt_inner=0
    for i in range(len(mp)):
        aux_cnt=0
        is_inside=False
        for j in range(len(mp[0])):
            if (i,j) not in loop:
                aux_cnt+=1
            else:
                #if vertical wall
                if loop[(i,j)]:
                    if is_inside:
                        cnt_inner+=aux_cnt
                    is_inside = not is_inside
                    aux_cnt = 0
    return cnt_inner

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
