import sys

def parse_data(data):
    lines = list(data.splitlines())
    time=''.join(lines[0][lines[0].find(':')+1:].strip().split())
    dist=''.join(lines[1][lines[1].find(':')+1:].strip().split())
    return (int(time), int(dist))

def ways_to_beat(race):
    time, dist = race
    cnt=0
    for press_t in range(time):
        new_dist=press_t*(time-press_t)
        if new_dist > dist:
            cnt+=1
    return cnt

def solve(data):
    race=parse_data(data)
    return (ways_to_beat(race))
    '''
    prod=1
    for race in data:
    print(data)
    return prod
    return 0
    '''

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
