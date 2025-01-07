from collections import defaultdict
import sys

I = {}
G = defaultdict(set)

def _parse(s):
  s=s.strip('=')
  s=s.strip()
  ss=s.split(' ')
  assert(len(ss)==2), s
  return int(ss[0].strip()), ss[1].strip()

ttt=_parse(' 18 KTJDG')
assert ttt == (18,'KTJDG'), ttt
assert _parse(' 1 VRPVC =') == (1,'VRPVC')

for l in sys.stdin:
  l = l.strip()
  if not l: continue
  s,t = l.split('>')
  tnum,tmat = _parse(t)
  ss=list(map(_parse,s.split(',')))
  assert tmat not in I
  I[tmat]=(tnum,ss)
  for _,mat in ss:
    G[tmat].add(mat)
