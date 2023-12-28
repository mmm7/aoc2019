import sys
import time
from collections import Counter

LS=6*25
#LS=2*3
I=[]

while True:
    layer = sys.stdin.read(LS)
    if len(layer)!=LS: break
    I.append(layer)

print(I)

DEC=[]
for i in range(LS):
    l=0
    while I[l][i]=='2': l+=1
    DEC.append(' X.'[int(I[l][i])])

for l in range(0,6*25,25):
    print(''.join(DEC[l:l+25]))
