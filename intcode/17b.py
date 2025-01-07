from collections import deque

from input import I
import intcode

def asciiline(s):
  r=[]
  for c in s:
    r.append(ord(c))
  r.append(10)
  return r

I=I[0]

mem=intcode.load(I)
# Wakeup.
assert mem[0]==1
mem[0]=2

output=[]
input=(
  asciiline('A,C,A,B,A,C,B,A,C,B') +
  asciiline('R,12,R,4,R,10,R,12') +
  asciiline('L,8,R,4,R,4,R,6') +
  asciiline('R,6,L,8,R,10') +
  asciiline('n')
)
intcode.run(0,mem,deque(input),output)
print(output)
