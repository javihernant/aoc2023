import sys

def positions_of_group(part, cnt, is_last):
    ps = []
    part_len = len(part)
    limit = part.find('#')
    if limit != -1:
        limit+=1
    else:
        limit = part_len

    for i in range(limit):
        if part[i] == '?' or part[i] == '#':
            is_pos=True
            j = i
            while (j< i+cnt):
                if j>=part_len or part[j] == '.':
                    is_pos=False
                    break
                j+=1
            if is_pos:
                if is_last and part[j:].find('#') != -1:
                    continue
                if j==part_len or part[j] != '#':
                    ps.append(i)
    return ps

def cnt_arrangements(record, groups, group_i):
    group_cnt=groups[group_i]
    is_last = group_i+1 == len(groups)
    pss = positions_of_group(record, group_cnt, is_last)
    if is_last:
        return len(pss)
    cnt=0
    for pos in pss:
        if pos+group_cnt+1 < len(record):
            tmp = cnt_arrangements(record[pos+group_cnt+1:], groups, group_i+1)
            if tmp == 0:
                continue
            cnt+=tmp
    return cnt

def solve(data):
    armts = 0
    for line in data.splitlines():
        record, _, groups = line.partition(' ')
        groups = groups.split(',')
        groups = [int(n) for n in groups]
        tmp = cnt_arrangements(record, groups, 0)
        armts += tmp

    return armts

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
