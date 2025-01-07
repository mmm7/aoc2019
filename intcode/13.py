from collections import deque,defaultdict

from input import I
import intcode

# 358: too high

I = I[0]

tiles=defaultdict(int)

def printboard(tiles):
  print('score:',tiles[(0,-1)])
  for y in range(20):
    l=[]
    for x in range(40):
      if tiles[(y,x)]==0: l.append(' ')
      if tiles[(y,x)]==1: l.append('X')
      if tiles[(y,x)]==2: l.append('#')
      if tiles[(y,x)]==3: l.append('=')
      if tiles[(y,x)]==4: l.append('O')
    print(''.join(l))

mem=intcode.load(I)
output=[]
input=None
pc=0
intcode.run(0,mem,input,output)

for i in range(0,len(output),3):
  x,y,t=output[i:i+3]
  tiles[(y,x)] = t

print(tiles)
printboard(tiles)

print('A:',sum(x == 2 for x in tiles.values()))

