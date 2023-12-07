import sys

def cnt_matches(line):
    line=line[line.find(':')+1:].strip()
    win_str, _, my_str = line.partition('|')
    win_nums = set(win_str.strip().split())
    my_nums = my_str.strip().split()
    cnt=0
    for num in my_nums:
        if num in win_nums:
            cnt+=1
    return cnt

def cnt_cards(idx, card_matches):
    cards=card_matches[idx]
    cnt=1
    for i in range(cards):
        cnt += cnt_cards(idx+i+1,card_matches)
    return cnt 

def solve(path):
    card_matches = []
    with open(path) as fp:
        for line in fp:
            card_matches.append(cnt_matches(line))
    cnt=0
    for i in range(len(card_matches)):
        cnt += cnt_cards(i, card_matches)
    return cnt

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    sol = solve(args[0])
    print("Solution:", sol)

if __name__ == '__main__':
    main(*sys.argv[1:])
