import sys

def hash_algo(step):
    curr = 0
    for c in step:
        curr += ord(c)
        curr *= 17
        curr %= 256
    return curr

def find_op(step):
    for i, c in enumerate(step):
        if c == '-' or c== '=':
            return i

def find_lens(box, label):
    for i, (lens_label, val) in enumerate(box):
        if lens_label==label:
            return i
    return -1

def store_lens(step, boxes):
    op = find_op(step)
    box = hash_algo(step[:op])
    if step[op] == '-':
        idx = find_lens(boxes[box], step[:op])
        if idx != -1:
            boxes[box].pop(idx)
    elif step[op] == '=':
        idx = find_lens(boxes[box], step[:op])
        if idx != -1:
            boxes[box][idx] = (step[:op], int(step[op+1:]))
        else:
            boxes[box].append((step[:op], int(step[op+1:])))

def solve(data):
    steps = data.strip('\n').split(',')
    boxes = [[] for _ in range(256)]
    for step in steps:
        store_lens(step, boxes)
    ans = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            ans+=(i+1)*(j+1)*(boxes[i][j][1])
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
