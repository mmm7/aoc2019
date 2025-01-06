from input import I

print(I)
assert len(I)==2, len(I)

DIR={
  'U': (-1,0),
  'D': (+1,0),
  'L': (0,-1),
  'R': (0,+1),
}

def segments(ws):
  seg=[]
  y,x=0,0
  for dir,dist in ws:
    dy,dx=tuple([x*dist for x in DIR[dir]])
    seg.append((
      (min(y,y+dy),min(x,x+dx)),
      (max(y,y+dy),max(x,x+dx))
    ))
    y,x=y+dy,x+dx
  return seg

def horiz(s):
  s1,s2=s
  if s1[0]==s2[0]: return True
  assert s1[1]==s2[1], s
  return False

def intersection(r,s):
  if not (horiz(r) ^ horiz(s)): return None
  if horiz(s): r,s=s,r
  # r: horizontal, s:vertical
  assert horiz(r),(r,s)
  assert not horiz(s),(r,s)
  r1,r2=r
  r1y,r1x=r1
  r2y,r2x=r2
  assert r1y==r2y, (r,s)
  s1,s2=s
  s1y,s1x=s1
  s2y,s2x=s2
  assert s1x==s2x, (r,s)

  if r1x<=s1x and s1x<=r2x and s1y<=r1y and r1y<=s2y:
    return (r1y,s1x)
  return None


S0 = segments(I[0])
S1 = segments(I[1])

intersections=set()
for s0 in S0:
  for s1 in S1:
    inter=intersection(s0,s1)
    #print(s0,s1,inter)
    if not inter: continue
    if inter==(0,0): continue
    intersections.add((abs(inter[0])+abs(inter[1]),inter))

print(sorted(intersections))
print('A:', sorted(intersections)[0][0])

points={}

y,x,w=0,0,0
for dir,dist in I[0]:
  dy,dx = DIR[dir]
  for _ in range(dist):
    y,x=y+dy,x+dx
    w+=1
    if (y,x) in points: continue
    points[(y,x)]=w

intersections=set()

y,x,w=0,0,0
for dir,dist in I[1]:
  dy,dx = DIR[dir]
  for _ in range(dist):
    y,x=y+dy,x+dx
    w+=1
    if (y,x) in points: intersections.add(points[y,x]+w)

print(sorted(intersections))

print('B:', sorted(intersections)[0])
