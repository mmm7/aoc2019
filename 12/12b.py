import math
from itertools import permutations

from input import I

def printall():
  for p in I:
    print(str(p))

def iterate():
  for a,b in permutations(I,2):
    a.pullby(b)
  for p in I:
    p.move()

def hashx():
  for p in I:
    yield p.x
    yield p.dx

def hashy():
  for p in I:
    yield p.y
    yield p.dy

def hashz():
  for p in I:
    yield p.z
    yield p.dz

HASHX=tuple(hashx())
HASHY=tuple(hashy())
HASHZ=tuple(hashz())

X,Y,Z=0,0,0
i=0
while True:
  i+=1
  iterate()
  if tuple(hashx())==HASHX:
    print ('x',i)
    if not X: X=i
  if tuple(hashy())==HASHY:
    print ('y',i)
    if not Y: Y=i
  if tuple(hashz())==HASHZ:
    print ('z',i)
    if not Z: Z=i
  if X and Y and Z: break

print('B:',math.lcm(X,Y,Z))
