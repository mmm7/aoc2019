import sys
import time
from collections import Counter

LS=6*25
#LS=2*3
I=[]

while True:
    layer = sys.stdin.read(LS)
    if len(layer)!=LS: break
    I.append(layer)

print(I)

def tocount(s):
  counter = Counter(s)
  return (counter['0'], counter['1'], counter['2'])

RES=sorted(list(map(tocount, I)))
print(RES)
print(RES[0][1]*RES[0][2])

