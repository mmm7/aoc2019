from collections import deque

from input import I
import intcode

I=I[0]

mem=intcode.load(I)
output=[]
intcode.run(0,mem,None,output)
print(output)
print(''.join(map(chr,output)))

IMG=[]
line=[]
for i in output:
  if i==10:
    if line: IMG.append(''.join(line))
    line=[]
    continue
  line.append(chr(i))

for l in IMG:
  print(l)

YS=len(IMG)
XS=len(IMG[0])

res=0
for y in range(1,YS-1):
  for x in range(1,XS-1):
    if (IMG[y][x]=='#' and
        IMG[y-1][x]=='#' and
        IMG[y+1][x]=='#' and
        IMG[y][x-1]=='#' and
        IMG[y][x+1]=='#'):
      res+=y*x

print('A:',res)
