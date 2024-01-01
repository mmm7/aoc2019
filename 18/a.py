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

def getpath(k,l):
  s,t  = POS[k], POS[l]
  vis = set()
  # (y,x), steps, doors
  bfs = deque([(s, 0, set())])
  while bfs:
    pos, steps, doors=bfs.popleft()
    doors = doors.copy()
    if pos == t: return steps, doors
    if pos in vis: continue
    vis.add(pos)
    y,x = pos
    c = I[y][x]
    if c == '#': continue
    if c.isupper(): doors.add(c.lower())
    for dx,dy in ((1,0), (-1,0), (0,1), (0,-1)):
      bfs.append(((y+dy, x+dx), steps+1, doors,))
  assert False, (k,l,s,t,doors,vis)

PATHS = defaultdict(dict)

for k in KEYS.union(set('@')):
  for l in KEYS:
    if l in PATHS[k]: continue
    if k == l: continue
    a,b = sorted([k,l])
    path = getpath(a,b)
    PATHS[a][b] = path
    PATHS[b][a] = path

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
  if curr in keys: return float("inf")
  dpkey = (curr, frozenset(keys))
  if dpkey in DP: return DP[dpkey]

  if len(keys) == len(KEYS): return 0

  keys.add(curr)
  ret = min([dist+collect(nex, keys, pa+[nex]) for nex,dist in neighbors(curr, keys)])
  print('==', curr, keys, pa, ret)
  keys.remove(curr)
  DP[dpkey] = ret
  return ret


print('1:', collect('@', set(), ['@']))
