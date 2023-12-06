import sys

def store_nums(nums, i, line):
    j=0
    while j<len(line):
        if line[j].isdigit():
            num=""
            start=j
            while line[j].isdigit():
                num+=line[j]
                j+=1
            if num:
                nums[(i,start)]=num
        else:
            j+=1

def store_symbols(syms, i, line):
    for j, c in enumerate(line):
        if c == '*':
            syms[(i,j)] = []

def group_adj(row, col, length, num, syms):
    for i in range(row-1, row+2):
        for j in range(col-1, col+length+1):
            if (i,j) in syms:
                syms[(i,j)].append(num)

def solve(path):
    nums={}
    syms={}
    with open(path) as fp:
        for i,line in enumerate(fp):
            store_nums(nums, i, line)
            store_symbols(syms, i, line)
    cnt=0
    for (i, j), num in nums.items():
        group_adj(i, j, len(num), int(num), syms)

    sol=0
    for adj_ls in syms.values():
        if (len(adj_ls) == 2):
            sol+=adj_ls[0]*adj_ls[1]
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    print(solve(args[0]))

if __name__ == '__main__':
    main(*sys.argv[1:])
