import sys

INC = 'deal with increment'
NEW = 'deal into new stack'
CUT = 'cut'

def _inc(x): return x,0
def _new(): return -1,-1
def _cut(x): return 1,-x

I = []
for l in sys.stdin:
  l = l.strip()
  if l.startswith(INC): I.append(_inc(int(l[len(INC):])))
  if l.startswith(NEW): I.append(_new())
  if l.startswith(CUT): I.append(_cut(int(l[len(CUT):])))

