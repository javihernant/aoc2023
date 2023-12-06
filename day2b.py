import sys

def process_game(i, line):
    line=line[line.find(':')+1:].strip()
    sets=line.split('; ')
    ball_cnt={}
    for s in sets:
        for ball in s.split(', '):
           ball=ball.split(' '); 
           if ball[1] not in ball_cnt:
               ball_cnt[ball[1]] = int(ball[0])
           elif int(ball[0]) > ball_cnt[ball[1]]:
               ball_cnt[ball[1]] = int(ball[0])
    power = 1
    for cnt in ball_cnt.values():
        power*=cnt
    return power

def solve(path):
    sol=0
    with open(path) as fp:
        for i,line in enumerate(fp):
            sol += process_game(i+1,line)
    return sol

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
