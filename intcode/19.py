from collections import deque

from input import I
import intcode

# 26249854 too high

I=I[0]

def runon(i):
  mem=intcode.load(I)
  output=[]
  intcode.run(0,mem,deque(i),output)
  assert len(output)==1
  assert output[0] in (0,1)
  return output[0]

cnt=0
for y in range(50):
  l=[]
  for x in range(50):
    o=runon([x,y])
    l.append('.#'[o])
    if o: cnt+=1
  print(''.join(l))

print('A:',cnt)

beam=dict()

SQUARE=100
START=15
y=START

x=0
o=0
while not o:
  #print('noto',x,y)
  x+=1
  o=runon([x,y])
l=x
while o:
  #print('o',x,y)
  x+=1
  o=runon([x,y])
h=x
beam[y]=(l,h)

print(beam)
while True:
#for _ in range(6):
  l,h=beam[y]
  y+=1
  while not runon([l,y]): l+=1
  while runon([h,y]): h+=1
  beam[y]=(l,h)
  #print(y,l,h)

  if y>START+SQUARE:
    #print (y,beam[y])
    if beam[y-SQUARE+1][1]>=beam[y][0]+SQUARE:
      break

print(y,beam[y],beam[y-SQUARE+1])

print('B:',beam[y][0]*10000+(y-SQUARE+1))
