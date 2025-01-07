from collections import deque

from input import I
import intcode

I = I[0]

panels={(0,0):1}
y,x=0,0
dy,dx=-1,0

mem=intcode.load(I)
pc=0

while True:
  input=deque([ (0,1)[(y,x) in panels and panels[(y,x)]==1] ])

  output=[]
  #print(mem,input,output)
  pc=intcode.run_until_next_output(pc,mem,input,output)
  if not output: break
  assert not input
  assert len(output)==1, output
  assert output[0] in (0,1), output
  panels[(y,x)]=output[0]

  output=[]
  pc=intcode.run_until_next_output(pc,mem,input,output)
  assert len(output)==1, output
  assert output[0] in (0,1), output
  # 0 means it should turn left 90 degrees, and 1 means it should turn right 90 degrees.
  if output[0]==0:
    dx,dy=dy,-dx
  else:
    dx,dy=-dy,dx
  x+=dx
  y+=dy

#print(panels)

for y in range(8):
  s=[]
  for x in range(80):
    if (y,x) in panels and panels[(y,x)]: s.append('#')
    else: s.append('.')
  print(''.join(s))
