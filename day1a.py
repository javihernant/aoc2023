import sys

def getnum(line):
    str_num = "" 
    for c in line:
        if c.isdigit():
            str_num += c
    return int(str_num[0] + str_num[len(str_num)-1])

def solve(path):
    sol=0
    with open(path) as fp:
        for line in fp:
            sol += getnum(line)
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
