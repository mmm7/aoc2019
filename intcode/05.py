from collections import deque

from input import I
import intcode

mem=intcode.load(I[0])

input=deque([1])
output=[]
intcode.run(0,mem,input,output)

print(mem)

print(output)
