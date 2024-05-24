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

def shortest_path(mp, init):
    visited = {}
    qu = deque([(init, 0)]);
    while qu:
        pos, steps = qu.popleft()
        if pos in visited:
            continue
        visited[pos] = steps
        if is_access(pos[0]+1, pos[1], mp):
            qu.append(((pos[0]+1, pos[1]), steps + 1))
        if is_access(pos[0]-1, pos[1], mp):
            qu.append(((pos[0]-1, pos[1]),steps + 1))
        if is_access(pos[0], pos[1]+1, mp):
            qu.append(((pos[0], pos[1] + 1), steps + 1))
        if is_access(pos[0], pos[1]-1, mp):
            qu.append(((pos[0], pos[1] - 1), steps + 1))
    return visited

def count_steps(visited, steps, mp):
    distance_to_edge = len(mp) // 2
    n = (steps - distance_to_edge) // len(mp)
    num_odd_grids = (n + 1) ** 2
    num_even_grids = n**2

    def num_points_where(cond):
        sum = 0
        for v, s in visited.items():
            if cond(s):
                sum += 1
        return sum

    odd_corners = num_points_where(lambda v: v % 2 != 0 and v > distance_to_edge)
    even_corners = num_points_where(lambda v: v % 2 == 0 and v > distance_to_edge)

    return (num_odd_grids * num_points_where(lambda v: v % 2 != 0)
            + num_even_grids * num_points_where(lambda v: v % 2 == 0)
            - ((n + 1) * odd_corners)
            + (n * even_corners))

def solve(data):
    mp = data.splitlines()
    init_pos = find_s(mp)
    visited = shortest_path(mp, init_pos)
    return count_steps(visited, 26501365, mp)

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
