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
