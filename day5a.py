import sys

def parse_map(text):
    conv=[]
    for line in text.splitlines():
        part=line.split()
        part=[int(n) for n in part]
        conv.append(part)
    return conv

def convert_el(el, conv):
    for data in conv:
        (dst, src, length)=data[0], data[1], data[2]
        dif=el-src
        if dif>=0 and dif<length:
            return dst+dif
    return el

def build_convs(data):
    convs=[]
    for i in range(len(data)):
        mp=data[i][data[i].find(':')+2:]
        conv=parse_map(mp)
        convs.append(conv)
    return convs

def solve(data):
    data=data.split("\n\n")
    seeds=data[0][data[0].find(':')+2:].split()
    seeds=[int(s) for s in seeds]
    convs=build_convs(data[1:])
    sol=-1
    for s in seeds:
        location=s
        for conv in convs:
            location=convert_el(location, conv)
        if sol<0 or location < sol:
            sol=location
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
