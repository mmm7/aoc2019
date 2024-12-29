import sys

I = []
A = set()

y=-1
for l in sys.stdin:
  y+=1
  l = l.strip()
  if not l: continue
  I.append(l)
  for x,c in enumerate(l):
    if c=='#': A.add((y,x))

YS=len(I)
XS=len(I[0])
