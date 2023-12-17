import sys

def parse_data(data):
    lines = []
    for line in data.splitlines():
        line = line.split()
        line = [int(val) for val in line]
        lines.append(line)
    return lines 

def calc_next_val(hist):
    all_zero=True
    for val in hist:
        if val != 0:
            all_zero=False
            break
    if all_zero:
        return 0
    next_hist = [j - i for i, j in zip(hist[:], hist[1:])]
    return hist[0] - calc_next_val(next_hist)

def solve(data):
    histories = parse_data(data)
    sol = 0
    for hist in histories:
        sol += calc_next_val(hist)
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
