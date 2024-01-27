import sys

'''
Another classic Pick's theorem problem, surprised to see this again after it
showed up on Day 10 again this year. The instructions in the input essentially
describe a polygon with integer vertices, and the number of cubic meters of
lava is the number of interior points of the polygon plus the number of
boundary points. You can count the number of boundary points by just adding up
all the distances in the instructions, and you can figure out the area by
applying shoelace formula to the vertices of the polygon. Once you have those
two pieces of information, apply Pick's theorem to get the number of interior
points, and then add the number of interior points to the number of boundary
points to get the answer.
'''

def parse_inst(inst):
    if inst == '0':
        return (0, 1)
    elif inst == '1':
        return (1, 0)
    elif inst == '2':
        return (0, -1)
    elif inst == '3':
        return (-1, 0)

def parse_input(data):
    i = 0
    j = 0
    dirs = []
    for line in data.splitlines():
        hx = line.split(' ')[2]
        cnt = int(hx[2:7], 16)
        dr = parse_inst(hx[7])
        dirs.append((cnt, dr))
    dirs = list(dirs)
    return dirs

def solve(data):
    dirs = parse_input(data)
    outter = 0
    for (l, _) in dirs:
        outter += l

    i = 0
    j = 0
    corner = []
    for (l, d) in dirs:
        i += d[0]*l
        j += d[1]*l
        corner.append((i,j))
    area = 0
    for i in range(len(corner) - 1):
        y1, x1 = corner[i]
        y2, x2 = corner[i+1]
        area += x1 * y2 - x2 * y1
        
    return abs(area) // 2 + outter // 2 + 1
    
def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
