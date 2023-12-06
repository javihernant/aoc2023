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
        if not c.isdigit() and c != '.' and c !='\n':
            syms.add((i,j))

def is_num_adj(row, col, length, syms):
    for i in range(row-1, row+2):
        for j in range(col-1, col+length+1):
            if (i,j) in syms:
                return True
    return False


def solve(path):
    nums={}
    syms=set()
    with open(path) as fp:
        for i,line in enumerate(fp):
            store_nums(nums, i, line)
            store_symbols(syms, i, line)
    cnt=0
    for (i, j), num in nums.items():
        if is_num_adj(i, j, len(num), syms):
            cnt+=int(num)
    return cnt

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    print(solve(args[0]))

if __name__ == '__main__':
    main(*sys.argv[1:])
