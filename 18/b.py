from collections import deque, defaultdict

import sys

I=[]

for line in sys.stdin.readlines():
  line = line.strip()
  if not line: continue
  I.append(line)

print(I)

ys = len(I)
xs = len(I[0])

POS = dict()

KEYS = set()

for y in range(ys):
  for x in range(xs):
    c = I[y][x]
    if c in '.#': continue
    assert c not in POS
    POS[c] = (y,x)
    if c.islower(): KEYS.add(c)

print(POS)
print(KEYS)

PATHS = defaultdict(dict)

def floodfrom(k):
  if not k in POS: return
  s  = POS[k]
  vis = set()
  # (y,x), steps, doors
  bfs = deque([(s, 0, set())])
  while bfs:
    pos, steps, doors=bfs.popleft()
    doors = doors.copy()
    if pos in vis: continue
    vis.add(pos)
    y,x = pos
    c = I[y][x]
    if c == '#': continue
    if c.isupper(): doors.add(c.lower())
    if c.islower():
      if steps != 0:
        PATHS[k][c] = (steps, doors)
    for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
      bfs.append(((y+dy, x+dx), steps+1, doors,))

for k in KEYS.union(set('@01234')):
  floodfrom(k)

print('PATHS', PATHS)

def neighbors(curr, keys):
  ret = set()
  for nex,(dist,doors) in PATHS[curr].items():
    if doors-keys: continue
    ret.add((nex,dist))
  return ret

print (neighbors('@', set()))

DP=dict()

def collect(curr, keys, pa):
  #keys = keys.copy()
  newkey = None
  for c in curr:
    if c not in keys:
      assert not newkey, (curr,keys,pa)
      newkey = c
  if not newkey: return float("inf")
  #print('------', curr, keys,pa, newkey)

  dpkey = (''.join(sorted(curr)), frozenset(keys))
  if dpkey in DP: return DP[dpkey]

  if len(keys) == len(KEYS)+3: return 0

  keys.add(newkey)

  # (nex, dist)
  candidates = []

  for i in range(len(curr)):
    for nex, dist in neighbors(curr[i], keys):
      cs = list(curr)
      cs[i] = nex
      candidates.append((cs, dist,))

  ret = min(map(lambda x: x[1]+collect(x[0], keys, pa+[x[0]]), candidates))
  print('==', curr, keys, pa, ret)
  keys.remove(newkey)

  DP[dpkey] = ret
  return ret


#print('1:', collect('@', set(), ['@']))
print('2:', collect('0123', set('123'), ['0123']))
