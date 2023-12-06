import sys

total = {"red": 12,
         "green": 13,
         "blue": 14}
def valid(balls):
    cnt = int(balls[0])
    col = balls[1]
    if cnt > total[col]:
        return False
    else:
        return True

def process_game(i, line):
    line=line[line.find(':')+1:].strip()
    sets=line.split('; ')
    for s in sets:
        for balls in s.split(', '):
           balls=balls.split(' '); 
           if not valid(balls):
               return 0
    return i

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
