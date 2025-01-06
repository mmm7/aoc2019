from collections import deque
from itertools import permutations

import intcode
from input import I

I=I[0]

"""
mem=intcode.load(I)
output=[]
input=deque([9,100,103,109])
#print(mem,input,output)
try:
  intcode.run(0,mem,input,output)
except IndexError:
  print(output)

mem=intcode.load(I)
pc=0

output=[]
pc=intcode.run_until_next_output(pc,mem,deque([9,100]),output)
print(output)

output=[]
pc=intcode.run_until_next_output(pc,mem,deque([103]),output)
print(output)

output=[]
pc=intcode.run_until_next_output(pc,mem,deque([109]),output)
print(output)
"""

cand=[]
for phases in permutations(range(5,10)):
  #print('=======================', phases)
  carry=0
  phases_copy=list(phases)
  states=[{'pc':0,'mem':intcode.load(I)} for _ in range(5)]
  idx=0
  while True:
    output=[]
    input=deque([carry])
    if phases_copy: input.appendleft(phases_copy.pop(0))
    pc = states[idx]['pc']
    mem = states[idx]['mem']
    #print(pc,mem,input,output)
    #print(f'{input=}')
    pc = intcode.run_until_next_output(pc,mem,input,output)
    #print(output)
    states[idx]['pc']=pc
    if not output: break
    assert len(output)==1
    carry=output[0]
    idx=(idx+1)%5
  cand.append((carry,tuple(phases)))

print('B:',sorted(cand)[-1])
