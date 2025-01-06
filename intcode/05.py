from collections import deque

from input import I
import intcode

def testinput(input):
  mem=intcode.load(I[0])
  print('================',input)
  output=[]
  intcode.run(0,mem,input,output)
  return output

"""
print(testinput(deque([0])))
print(testinput(deque([5])))
print(testinput(deque([7])))
print(testinput(deque([8])))
print(testinput(deque([9])))
print(testinput(deque([10])))
"""

print('A')
print(testinput(deque([1])))
print('B')
print(testinput(deque([5])))
