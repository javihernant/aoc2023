import sys
from functools import cmp_to_key

def parse_data(data):
    hands=[]
    for line in data.splitlines():
        aux = line.split()
        aux=(aux[0], int(aux[1]))
        hands.append(aux)
    return hands 

def get_type(hand):
    dic = {}
    for c in hand:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1
    dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    if len(dic) == 1:
        return 7
    if len(dic) == 5:
        return 1
    if len(dic) == 2 and dic[0][1] == 4:
        return 6
    if len(dic) == 2 and dic[0][1] == 3:
        return 5
    if dic[0][1] == 3:
        return 4
    if dic[0][1] == 2 and dic[1][1] == 2:
        return 3
    if dic[0][1] == 2:
        return 2
    return 0

labels=['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def compare(a,b):
    hand_a, _ = a
    hand_b, _ = b
    type_a = get_type(hand_a)
    type_b = get_type(hand_b)
    if type_a > type_b:
        return 1
    elif type_a < type_b:
        return -1
    else:
        for i in range(len(hand_a)):
            aux_a=labels.index(hand_a[i])
            aux_b=labels.index(hand_b[i])
            if aux_a < aux_b:
                return 1
            elif aux_a > aux_b:
                return -1
        return 0



def solve(data):
    data=parse_data(data)
    data = sorted(data, key=cmp_to_key(compare))
    sol=0
    for i, (_,bid) in enumerate(data):
        sol += (i+1)*bid
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
