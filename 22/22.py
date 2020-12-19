import sys

N = 10007

INC = 'deal with increment'
NEW = 'deal into new stack'
CUT = 'cut'

def _lin(t, a, b):
  return (a*t+b)%N

def _inc(t, x):
  return _lin(t,x,0)
  return (t*x)%N

def _new(t):
  return _lin(t,-1,-1)
  return (-t-1)%N

def _cut(t, x):
  return _lin(t,1,-x)
  return (t-x)%N

t = 2019

for l in sys.stdin:
  l = l.strip()
  if l.startswith(INC): t = _inc(t, int(l[len(INC):]))
  if l.startswith(NEW): t = _new(t)
  if l.startswith(CUT): t = _cut(t, int(l[len(CUT):]))

print(t)
