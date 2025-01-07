import time
from collections import deque,defaultdict

from input import I
import intcode

# 13282: too low

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
mem[0]=2  # Insert coin.

pc=0

pad=None
ball=None
inp=0
tick=-1
while True:
  tick+=1
  input=deque([inp])

  output=[]
  pc=intcode.run_until_next_output(pc,mem,input,output)
  if not output: break
  x=output[0]

  output=[]
  pc=intcode.run_until_next_output(pc,mem,input,output)
  if not output: break
  y=output[0]

  output=[]
  pc=intcode.run_until_next_output(pc,mem,input,output)
  if not output: break
  t=output[0]

  tiles[(y,x)] = t
  if t==4: ball = x
  if t==3: pad  = x

  if ball and pad:
    if ball==pad: inp=0
    if ball>pad: inp=1
    if pad>ball: inp=-1

  """
  if tiles[(19,37)]:
    printboard(tiles)
    time.sleep(0.2)
  """
  if tick%100==0:
    printboard(tiles)

printboard(tiles)

print('B:',tiles[(0,-1)])
