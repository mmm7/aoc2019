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

print(res)

print(sorted([(len(A)-len(y)-1,x) for x,y in res.items()]))
