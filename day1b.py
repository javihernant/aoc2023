import sys

def to_dig(line):
    if line.startswith("zero"):
        return "0"
    elif line.startswith("one"):
        return "1"
    elif line.startswith("two"):
        return "2"
    elif line.startswith("three"):
        return "3"
    elif line.startswith("four"):
        return "4"
    elif line.startswith("five"):
        return "5"
    elif line.startswith("six"):
        return "6"
    elif line.startswith("seven"):
        return "7"
    elif line.startswith("eight"):
        return "8"
    elif line.startswith("nine"):
        return "9"
    else:
        return ""

def getnum(line):
    str_num = "" 
    for i,c in enumerate(line):
        if c.isdigit():
            str_num += c
        else:
            str_num += to_dig(line[i:])
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
