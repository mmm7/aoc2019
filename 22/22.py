from input import I

N = 10007

def _lin(t, a, b):
  return (a*t+b)%N

t = 2019
for a,b in I: t = _lin(t,a,b)
print('1--->',t)

