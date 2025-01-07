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

for i in range (1001):
  print('===================',i)
  printall()
  print('Energy:', sum(map(lambda x:x.energy(), I)))
  iterate()
