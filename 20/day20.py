from input import I,P,AA,ZZ

print(AA, ZZ, P)

step = 0
vis = {AA}
pos = [AA]

def valid(y,x):
    global I
    if I[y][x]!='.': return False
    if (y,x) in vis: return False
    return True

while True:
    step += 1
    newpos = []
    if len(pos) == 0: break
    for y,x in pos:
        targets = [(y+1,x),(y-1,x),(y,x+1),(y,x-1)]
        if (y,x) in P: targets.append(P[(y,x)])
        for yy,xx in targets:
            if (yy,xx) == ZZ:
                print('1:', step)
            if not valid(yy,xx): continue
            vis.add((yy,xx))
            newpos.append((yy,xx))
    pos = newpos
