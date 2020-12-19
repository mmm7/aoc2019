from functools import reduce
from input import I

MOD = 10007

def _lin(t, a, b):
  return (a*t+b)%MOD

t = 2019
for a,b in I: t = _lin(t,a,b)
print('1--->',t)

# (B1) Full shuffle
#
# f(x) = ax + b
# g(x) = cx + d
# g(f(x)) = g(ax+b) = c*(ax+b)+d = c*a*x + c*b + d = [c*a]x + [c*b+d]

def collapse(mod):
  def c(f,g):
    a,b = f
    c,d = g
    return (c*a)%mod, (c*b+d)%mod
  return c

assert collapse(7)((3,4),(5,6))==(1,5)

shuffle1 = reduce(collapse(MOD), I)
print('1--->',(2019*shuffle1[0]+shuffle1[1])%MOD)

MOD=119315717514047      # prime
N=101741582076661  # prime

a,b = reduce(collapse(MOD), I)
print('shuffle:',a,b)

# (B2) N times
#
# f(x) = ax + b
# f(f(x)) = a(ax+b)+b = [a**2]x +  ab + b
# f(f(f(x))) = [a**3]x + [a**2]*b + [a**1]*b + [a**0]*b
# f^n(x) = [a**n]x + [a**(n-1) + ... + a**(0)] b = [a**n]x + Sb
# (a-1)*S = aS - S = a**n - 1
# S = (a**n - 1) / (a-1)

# https://stackoverflow.com/a/4798776
def modinv(a, p):
  return pow(a,p-2,p)

assert modinv(5,7)==3, modinv(5,7)
assert modinv(101741582076661, 119315717514047)==15359977617634, modinv(101741582076661, 119315717514047)

# python 3.8
#a,b = pow(a,N,MOD), (pow(a,N,MOD)-1)%MOD * (pow(a-1,-1,MOD) * b)%MOD
a,b = pow(a,N,MOD), ((pow(a,N,MOD)-1) * modinv(a-1,MOD) * b)%MOD

print('N times:', a,b)

# (B3) Inverse
#
# f(x) = ax + b
# ax = f(x) - b
# x = (f(x) - b) / a

print('2--->', ((2020 - b) * modinv(a,MOD)) % MOD)
