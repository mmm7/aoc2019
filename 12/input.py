import sys

I = []

def _pull(p, other):
    if other>p: return 1
    if other<p: return -1
    return 0

class Moon(object):
  def __init__(self, s):
    s = s.strip('<>')
    co=s.split(',')
    assert len(co)==3, s
    self.x=int(co[0].split('=')[1])
    self.y=int(co[1].split('=')[1])
    self.z=int(co[2].split('=')[1])

    self.dx=0
    self.dy=0
    self.dz=0

  def __str__(self):
    return '[pos(%d,%d,%d)/vel(%d,%d,%d)]' % (self.x,self.y,self.z,self.dx,self.dy,self.dz)

  def move(self):
    self.x+=self.dx
    self.y+=self.dy
    self.z+=self.dz

  def pullby(self, other):
    self.dx+=_pull(self.x,other.x)
    self.dy+=_pull(self.y,other.y)
    self.dz+=_pull(self.z,other.z)

for l in sys.stdin:
  l = l.strip()
  if not l: continue
  I.append(Moon(l))
