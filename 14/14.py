from collections import defaultdict
from graphlib import TopologicalSorter
from input import I,G

print(I)

#print(G)
ts = list(TopologicalSorter(G).static_order())
#print(ts)

assert ts[-1]=='FUEL',ts
assert ts[0]=='ORE',ts

req=defaultdict(int)
req['FUEL']=1

while ts:
  tmat=ts.pop()
  need=req[tmat]
  print(f'{tmat=},{need=}')
  assert need>0
  if tmat=='ORE': break
  tnum,ss = I[tmat]
  mult = (need+tnum-1)//tnum
  print(f'{tnum=},{mult=},{ss=}')
  assert mult*tnum>=need
  for snum,smat in ss:
    req[smat]+=snum*mult

print('A:', req['ORE'])
