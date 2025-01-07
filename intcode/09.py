from collections import deque

from input import I
import intcode

I = I[0]

mem=intcode.load(I)
output=[]
input=deque([1])
#print(mem,input,output)
intcode.run(0,mem,input,output)

print('A:',output)

mem=intcode.load(I)
output=[]
input=deque([2])
#print(mem,input,output)
intcode.run(0,mem,input,output)

print('B:',output)
