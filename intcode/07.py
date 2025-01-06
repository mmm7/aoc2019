from collections import deque
from itertools import permutations

import intcode
from input import I

I=I[0]

cand=[]
for phases in permutations(range(5)):
  carry=0
  pc=list(phases)
  while pc:
    mem=intcode.load(I)
    output=[]
    input=deque([pc.pop(),carry])
    print(mem,input,output)
    intcode.run(0,mem,input,output)
    assert len(output)==1
    carry=output[0]
  cand.append((carry,tuple(reversed(phases))))

print(sorted(cand))
