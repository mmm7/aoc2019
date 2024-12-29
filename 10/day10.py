import math
from collections import defaultdict

from input import I,A,XS,YS

print(A)
print(len(A))
print(YS,XS)

res=defaultdict(set)

def blinds(a1,a2):
  y,x=a1
  y2,x2=a2
  dy=y2-y
  dx=x2-x
  g=math.gcd(dy,dx)
  dy,dx=dy//g,dx//g
  while True:
    y2+=dy
    x2+=dx
    if x2<0 or y2<0 or x2>=XS or y2>=YS: break
    yield (y2,x2)

ttt=list(blinds((3,3),(2,2)))
assert ttt==[(1,1),(0,0)]
ttt=list(blinds((12,12),(2,2)))
assert ttt==[(1,1),(0,0)]

for a1 in A:
  for a2 in A:
    if a1==a2: continue
    for b in blinds(a1,a2):
      if b in A: res[b].add(a1)


res = sorted([(len(A)-len(y)-1,x) for x,y in res.items()])
print(res)

center=res[-1][1]

print('A:',res[-1][0])

print(center)

A.remove(center)

# https://stackoverflow.com/questions/14066933/direct-way-of-computing-the-clockwise-angle-between-two-vectors/16544330#16544330
# dot = x1*x2 + y1*y2      # Dot product between [x1, y1] and [x2, y2]
# det = x1*y2 - y1*x2      # Determinant
# angle = atan2(det, dot)  # atan2(y, x) or atan2(sin, cos)

def angle(center,t):
  x1,y1=center
  x2,y2=t
  #return math.atan2(x1*y2 - y1*x2, x1*x2 + y1*y2)
  return math.atan2(y2-y1, x2-x1)/math.pi

# 1.0 0.9954530252128411 0.5 0.0 -0.5 -0.9954530252128411
kor_test=[
  angle((0,0), (-7,0)),
  angle((0,0), (-70,1)),
  angle((0,0), (0,1)),
  angle((0,0), (1,0)),
  angle((0,0), (0,-2)),
  angle((0,0), (-70,-1)),
]
print(kor_test)
assert sorted(kor_test, reverse=True)==kor_test, sorted(kor_test, reverse=True)

def dist(a,b):
  y1,x1=a
  y2,x2=b
  return (y1-y2)*(y1-y2)+(x1-x2)*(x1-x2)

angles=defaultdict(list)
for a in A:
  angles[angle(center,a)].append((dist(center,a), a))
  angles[angle(center,a)].sort()

#print(angles)


keyed = []
for ang,v in angles.items():
  for i,vv in enumerate(v):
    dist,point = vv
    keyed.append((i,-ang,point))

keyed.sort()

#print(keyed)


bres=None
for i,dest in enumerate(keyed):
  #print(i+1, dest[2][1], dest[2][0])
  if i+1==200: bres=100*dest[2][1]+dest[2][0]

print("B:", bres)

