import sys

def parse_wkfs(data):
    wkfs = {}
    for line in data.splitlines():
        idx = line.find('{')
        name = line[:idx]
        tmp = line[idx+1:-1]
        wf = []
        for cond in tmp.split(','):
            idx = cond.find(':')
            if idx < 0:
                wf.append(('', '', 0, cond))
            else:
                wf.append((cond[0], cond[1], int(cond[2:idx]), cond[idx+1:]))
        wkfs[name] = wf
    return wkfs


def parse_pcs(data):
    pcs = []
    for line in data.splitlines():
        line = line[1:-1]
        line = line.split(',')
        pc = {}
        for v in line:
            pc[v[0]] = int(v[2:])
        pcs.append(pc)
    return pcs

def rate_pc(pc, wkfs):
    init = 'in'
    while init != 'R' and init != 'A':
        wf = wkfs[init]
        for (var, op, num, addr) in wf:
            if var == '':
                init = addr
                break
            else:
                a = pc[var]
                if op == '<':
                    if a < num:
                        init = addr
                        break
                else:
                    if a > num:
                        init = addr
                        break

    rating = 0
    if addr == 'A':
        for x in pc.values():
            rating += x
    return rating

def solve(data):
    data = data.strip()
    wkfs, _, pcs = data.partition('\n\n')
    wkfs = parse_wkfs(wkfs)
    pcs = parse_pcs(pcs)
    cnt = 0
    for pc in pcs:
        cnt += rate_pc(pc, wkfs)
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
