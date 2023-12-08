import sys

def parse_map(text):
    conv=[]
    for line in text.splitlines():
        part=line.split()
        part=[int(n) for n in part]
        conv.append(part)
    return conv

def build_convs(data):
    convs=[]
    for i in range(len(data)):
        mp=data[i][data[i].find(':')+2:]
        conv=parse_map(mp)
        convs.append(conv)
    return convs

def split_ranges(seeds, conv):
    conv = sorted(conv, key=lambda mp: mp[1])
    rngs=[]
    for rng_i, rng_len in seeds:
        rngs_aux=[]
        rng_i_aux=rng_i
        rng_len_aux=rng_len
        for mp in conv:
            (mp_dst, mp_src, mp_len)=mp[0], mp[1], mp[2]
            if rng_i_aux < mp_src:
                cnt=mp_src-rng_i_aux
                cnt=rng_len_aux if rng_len_aux < cnt else cnt
                rngs_aux.append((rng_i_aux, cnt))
                rng_i_aux+=cnt
                rng_len_aux-=cnt
            if rng_len_aux == 0:
                break
            if rng_i_aux >= mp_src and rng_i_aux < mp_src + mp_len:
                offset = rng_i_aux - mp_src
                cnt=rng_len_aux if rng_len_aux < mp_len-offset else mp_len - offset
                rngs_aux.append((mp_dst+offset, cnt))
                rng_len_aux -= cnt
                rng_i_aux += cnt
                if rng_len_aux == 0:
                    break
        if rng_len_aux > 0:
            rngs_aux.append((rng_i_aux, rng_len_aux))
        rngs.extend(rngs_aux)
    return rngs

def solve(data):
    data=data.split("\n\n")
    seeds=data[0][data[0].find(':')+2:].split()
    seeds=[(int(seeds[i]), int(seeds[i+1])) for i in range(0, len(seeds), 2)]
    convs=build_convs(data[1:])

    new_ranges=seeds
    for conv in convs:
        new_ranges=split_ranges(new_ranges, conv)
    sol=min(new_ranges, key=lambda rng:rng[0])[0]
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
