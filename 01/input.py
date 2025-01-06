import sys

I = []
for l in sys.stdin:
  l = l.strip()
  if not l: continue
  I.append(int(l))
