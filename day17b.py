import sys
from collections import deque

def parse_grid(data):
    return [[int(c) for c in line] for line in data.splitlines()]

def solve(data):
    grid = parse_grid(data)
    w = len(grid[0])
    h = len(grid)
    visited = {}
    pending = deque([(0,0, True), (0,0, False)])
    while (len(pending) != 0):
        node = pending.popleft()
        #check if vertical
        if node[2]:
            dist = visited[node] if node in visited else 0
            for j in range(1, 11):
                pos = (node[0], node[1] + j, not node[2])
                if pos[1] >= w:
                    break
                dist += grid[pos[0]][pos[1]]
                if j > 3:
                    if (pos not in visited
                        or ( visited[pos] > dist)):
                        visited[pos] = dist
                        pending.append(pos)

            dist = visited[node] if node in visited else 0
            for j in range(-1, -11, -1):
                pos = (node[0], node[1] + j, not node[2])
                if pos[1] < 0:
                    break
                dist += grid[pos[0]][pos[1]]
                if j < -3:
                    if (pos not in visited
                        or visited[pos] > dist):
                        visited[pos] = dist
                        pending.append(pos)
        else:
            dist = visited[node] if node in visited else 0
            for i in range(1, 11):
                pos = (node[0] + i, node[1], not node[2])
                if pos[0] >= h:
                    break
                dist += grid[pos[0]][pos[1]]
                if i > 3:
                    if (pos not in visited
                        or visited[pos] > dist):
                        visited[pos] = dist
                        pending.append(pos)

            dist = visited[node] if node in visited else 0
            for i in range(-1, -11, -1):
                pos = (node[0] + i, node[1], not node[2])
                if pos[0] < 0:
                    break
                dist += grid[pos[0]][pos[1]]
                if i < -3:
                    if (pos not in visited
                        or visited[pos] > dist):
                        visited[pos] = dist
                        pending.append(pos)

    a = visited[(h-1, w-1, True)] if (h-1, w-1, True) in visited else None
    b = visited[(h-1, w-1, False)] if (h-1, w-1, False) in visited else None
    res = None
    if not a:
        return b
    if not b:
        return a
    return a if a < b else b

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
