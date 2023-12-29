import sys

def count_rocks(data):
    lines = data.splitlines()
    h = len(lines)
    w = len(lines[0])
    count = [0 for _ in range(h)]
    last = [0 for _ in range(w)]
    for i,line in enumerate(lines):
        for j in range(w):
            if line[j] == 'O':
                count[last[j]] += 1
                last[j]+=1
            elif line[j] == '#':
                last[j] = i+1
    return count

def solve(data):
    ans = 0
    rocks = count_rocks(data)
    for i in range(len(rocks)):
        val = len(rocks) - (i)
        ans += val*rocks[i]
    return ans

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
