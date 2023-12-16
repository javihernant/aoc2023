import sys
from functools import reduce
from math import lcm

def parse_data(data):
    lines=data.splitlines()
    dirs = lines[0]
    nodes = {}
    for line in lines[2:]:
        src, _, dst = line.partition('=')
        src = src.strip()
        dst = dst.strip()
        dst = dst[1:dst.find(')')]
        dst_l, _, dst_r = dst.partition(',')
        dst_l = dst_l.strip()
        dst_r = dst_r.strip()
        nodes[src] = (dst_l, dst_r)
    return (dirs, nodes) 

def get_starting_nodes(nodes):
    start=[]
    for node, dst in nodes.items():
        if node[2] == 'A':
            start.append(dst)
    return start

def count_steps(dirs, nodes):

    start = get_starting_nodes(nodes)
    steps_per_path = []
    for node in start:
        steps = 0
        dir_idx = 0
        dir_len = len(dirs)
        next_st = node
        while True:
            d = dirs[dir_idx]
            if d == 'L':
                d = 0
            else:
                d = 1
            nxt = next_st[d]
            next_st = nodes[nxt]
            steps += 1
            dir_idx = (dir_idx+1) % dir_len
            if nxt[2] == 'Z':
                steps_per_path.append(steps)
                break
    return lcm(*steps_per_path)

def solve(data):
    dirs, nodes =parse_data(data)
    sol = count_steps(dirs, nodes)
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
