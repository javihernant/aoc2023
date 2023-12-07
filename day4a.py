import sys

def card_points(line):
    line=line[line.find(':')+1:].strip()
    win_str, _, my_str = line.partition('|')
    win_nums = set(win_str.strip().split())
    my_nums = my_str.strip().split()
    points=0
    for num in my_nums:
        if num in win_nums:
            if points == 0:
                points+=1
            else:
                points*=2
    return points

def solve(path):
    sol=0
    with open(path) as fp:
        for line in fp:
            sol += card_points(line)
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
