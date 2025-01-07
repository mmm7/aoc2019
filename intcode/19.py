from collections import deque

from input import I
import intcode

I=I[0]

def runon(i):
  mem=intcode.load(I)
  output=[]
  intcode.run(0,mem,deque(i),output)
  return output

cnt=0
for y in range(50):
  l=[]
  for x in range(50):
    o=runon([x,y])
    assert len(o)==1
    o=o[0]
    assert o in (0,1)
    l.append('.#'[o])
    if o: cnt+=1
  print(''.join(l))

print('A:',cnt)
