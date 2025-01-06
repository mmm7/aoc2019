from collections import defaultdict

from input import I

#print(I)

orbdict=defaultdict(list)

for s,d in I:
  assert d!='COM'
  orbdict[s].append(d)

orbs={'COM':0}

def dfs(p):
  assert p in orbs
  n=orbs[p]
  for moon in orbdict[p]:
    assert moon not in orbs
    orbs[moon]=n+1
    dfs(moon)

dfs('COM')

#print(orbs)

print('A:',sum(orbs.values()))


revdict={}
for s,d in I:
  revdict[d]=s

def path(p):
  if p=='COM': return ['COM']
  return path(revdict[p])+[p]

#print(path('YOU'))
#print(path('SAN'))

you=set(path('YOU'))
san=set(path('SAN'))

print('B:',2*len(you|san)-len(you)-len(san)-2)
