import sys

def look_horizontal(chunk):
    rows=chunk.splitlines()
    w=len(rows[0])
    h=len(rows)
    j=0
    while (j<w-1):
        i=0
        while (i < h):
            row=rows[i]
            a_i=j
            b_i=j+1
            row_reflect=True
            while (a_i >= 0):
                if b_i >= w:
                    break
                a=row[a_i]
                b=row[b_i]
                if (a != b):
                    row_reflect=False
                    break
                a_i -=1
                b_i +=1
            if not row_reflect:
                break
            i+=1
        if i==h:
            return j+1
        j+=1
    return -1

def look_vertical(chunk):
    rows=chunk.splitlines()
    w=len(rows[0])
    h=len(rows)
    i=0
    while (i<h-1):
        a_i=i
        b_i=i+1
        while (a_i >= 0):
            if b_i >= h:
                break
            a=rows[a_i]
            b=rows[b_i]
            if a != b:
                break
            a_i -=1
            b_i +=1
        if a_i == -1 or b_i == h:
            return i+1
        i+=1
    return -1

def find_reflection(chunk):
    res = look_horizontal(chunk)
    if res!=-1:
        return res

    res = look_vertical(chunk)
    if res!=-1:
        return 100*res
    return -1

def solve(data):
    ans = 0
    chunks = data.split('\n\n')
    for chunk in chunks:
        ans += find_reflection(chunk)
    return ans

def main(*args):
    if len(args) != 1:
        print("Enter path to file")
        return
    with open(args[0]) as fp:
        data=fp.read()
    print(solve(data))

if __name__ == '__main__':
    main(*sys.argv[1:])
