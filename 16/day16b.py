from input import I

from itertools import islice

#    80871224585914546619083218645595 becomes 24176176.
#    19617804207202209144916044189917 becomes 73745418.
#    69317163492948606335995924319873 becomes 52432133.

# B
# 10000*650 = 6500000
# Offset:     5979673

I=I[0]

offset=int(I[:7])
print(offset)

I=list(map(int,I))
print(I)
l=I * 10000
print(len(l))
assert offset>len(l)/2

def iterate(l):
  s=0
  ret=[]
  for n in range(len(l)-1,-1,-1):
    s+=l[n]
    s=s%10
    ret.append(s)
  return list(reversed(ret))

b=l[offset:].copy()

for i in range(100):
  print(i)
  b=iterate(b)

print(''.join(map(str,b[:8])))
