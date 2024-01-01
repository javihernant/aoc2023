import sys

def hash_algo(step):
    curr = 0
    for c in step:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

def solve(data):
    ans = 0
    steps = data.strip('\n').split(',')
    for step in steps:
        ans += hash_algo(step)
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
