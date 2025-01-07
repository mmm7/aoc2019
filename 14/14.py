from collections import defaultdict
from graphlib import TopologicalSorter
from input import I,G

print(I)

#print(G)
TS = tuple(TopologicalSorter(G).static_order())
#print(ts)

assert TS[-1]=='FUEL',TS
assert TS[0]=='ORE',TS


def orenum(fuelnum):
 req=defaultdict(int)
 req['FUEL']=fuelnum
 ts=list(TS)
 while ts:
  tmat=ts.pop()
  need=req[tmat]
  #print(f'{tmat=},{need=}')
  assert need>0
  if tmat=='ORE': break
  tnum,ss = I[tmat]
  mult = (need+tnum-1)//tnum
  #print(f'{tnum=},{mult=},{ss=}')
  assert mult*tnum>=need
  for snum,smat in ss:
    req[smat]+=snum*mult
 return req['ORE']

asol=orenum(1)
print('A:', asol)

TARGET=1000000000000
l,h=1,TARGET*asol

while l+1<h:
  assert orenum(l)<TARGET
  assert orenum(h)>=TARGET
  m = (l+h)//2
  ore=orenum(m)
  if ore<TARGET:
    l=m
  else:
    h=m

assert l+1==h, (l,h)
print('B:',l)
