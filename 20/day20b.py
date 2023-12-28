from input import I,P,AA,ZZ

print(AA, ZZ, P)

step = 0
vis = {(AA[0], AA[1], 0)}
pos = [(AA[0], AA[1], 0)]

def valid(y,x,level):
    global I
    if I[y][x]!='.': return False
    if (y,x,level) in vis: return False
    return True

while True:
    step += 1
    newpos = []
    if len(pos) == 0: break
    #print(pos)
    for y,x,l in pos:
        targets = [(y+1,x,l),(y-1,x,l),(y,x+1,l),(y,x-1,l)]
        if (y,x) in P:
            otherend = P[(y,x)]
            if x<=3 or y<=3 or y>=len(I)-4 or x>=len(I[0])-4: otherlevel = l-1
            else: otherlevel = l+1
            if otherlevel>=0:
                targets.append((P[(y,x)][0], P[(y,x)][1], otherlevel))
        for yy,xx,ll in targets:
            if (yy,xx) == ZZ and l==0:
                print('2:', step)
                exit(0)
            if not valid(yy,xx,ll): continue
            vis.add((yy,xx,ll))
            newpos.append((yy,xx,ll))
    pos = newpos
