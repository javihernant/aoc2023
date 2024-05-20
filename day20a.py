import sys
import re
from collections import deque


def run(m, kinds, ffs, cjs):
    queue = deque([("broadcaster", "button", 0)])
    low = 0
    high = 0
    while(queue):
        mod, from_mod, sig = queue.popleft()
        if sig:
            high += 1
        else:
            low += 1
        if mod not in kinds or (kinds[mod] == 0 and sig == 1):
            continue
        k = kinds[mod]
        if k == 2:
            for to_mod in m[mod]:
                queue.append((to_mod, mod, sig))
        elif k == 0:
            ffs[mod] = 0 if ffs[mod] else 1
            new_sig = ffs[mod]
            for to_mod in m[mod]:
                queue.append((to_mod, mod, new_sig))
        elif k == 1:
            cjs[mod][from_mod] = sig
            new_sig = 0
            for state in cjs[mod].values():
                if state == 0:
                    new_sig = 1
                    break
            for to_mod in m[mod]:
                queue.append((to_mod, mod, new_sig))
        else:
            print("error")
    # print(low, high)
    return (low,high)

def solve(data):
    m, kinds = get_map_and_kinds(data)
    ffs =  get_ffs(m, kinds)
    cjs =  get_cjs(m, kinds)
    low = 0
    high = 0
    for _ in range(1000):
        llow, lhigh = run(m, kinds, ffs, cjs)
        low += llow
        high += lhigh
    return low * high

#ffp % = 0
#conj % = 1
#broadcaster = 2
def get_map_and_kinds(data):
    patt = r"(?:(broadcaster)|(?:([%&])([a-z]+))) -> (.+)"
    m = {}
    kinds = {}
    for line in data.splitlines():
        match_obj = re.search(patt, line)
        if match_obj:
            broadcaster, kind, name, ls  = match_obj.groups()
            dest = ls.split(", ")
            if broadcaster and not name:
                name = "broadcaster"
            if kind == '%':
                kinds[name] = 0
            elif kind == '&':
                kinds[name] = 1
            else:
                kinds[name] = 2
            m[name] = dest
    return (m, kinds)

def get_ffs(m, kinds):
    ffs = {}
    for k, _ in m.items():
        if kinds[k] == 0:
            ffs[k] = 0
    return ffs

def get_cjs(m, kinds):
    cjs = {}
    for k, _ in m.items():
        if kinds[k] == 1:
            cjs[k] = { con: 0 for con in mods_to(k, m)}
    return cjs

def mods_to(final_mod, all_mods):
    ls = []
    for mod, cons in all_mods.items():
        if mod != final_mod:
            for con in cons:
                if con == final_mod:
                    ls.append(mod)
    return ls

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
