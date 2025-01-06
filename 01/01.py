from input import I

def fuel(x):
  return x//3-2

print('A:', sum(map(fuel,I)))

res=0
for i in I:
  f=i
  while True:
    f=fuel(f)
    if f<=0: break
    res+=f

print('B:', res)
