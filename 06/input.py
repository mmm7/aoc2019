import sys

def iproc(s):
  assert s[0] in 'UDLR'
  return(s[0], int(s[1:]))

I = []
for l in sys.stdin:
  l = l.strip()
  if not l: continue
  l = l.split(')')
  assert len(l)==2
  I.append(tuple(l))
