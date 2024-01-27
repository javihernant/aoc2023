import sys

def parse_input(data):
    min_i = 0
    max_i = 0
    min_j = 0
    max_j = 0
    i = 0
    j = 0
    mp = {}
    last = None
    for line in data.splitlines():
        line = line.split(' ')
        cnt = int(line[1])
        for offset in range(cnt):
            if line[0] == 'U':
                i -= 1
                if i < min_i:
                    min_i = i
                mp[(i,j)] = True
            elif line[0] == 'D':
                if not last or last == 'R' or last == 'L':
                    mp[(i,j)] = True
                i += 1
                if i > max_i:
                    max_i = i
                mp[(i,j)] = True
            elif line[0] == 'L':
                if last == 'D':
                    mp[(i,j)] = False
                j -= 1
                if j < min_j:
                    min_j = j
                mp[(i,j)] = False
            elif line[0] == 'R':
                if last == 'D':
                    mp[(i,j)] = False
                j += 1
                if j > max_j:
                    max_j = j
                mp[(i,j)] = False
            last = line[0]
    return (mp, min_i, max_i, min_j, max_j)

def solve(data):
    mp, min_i, max_i, min_j, max_j = parse_input(data)
    cnt = 0
    for i in range(min_i, max_i + 1):
        inside = False
        aux_cnt=0
        for j in range(min_j, max_j + 1):
            if (i,j) not in mp:
                aux_cnt +=1
            else:
                cnt+=1
                #if vertical wall
                if mp[(i,j)]:
                    if inside:
                        cnt += aux_cnt
                        aux_cnt = 0
                        inside = False
                    else:
                        aux_cnt = 0
                        inside = True
    return cnt

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
