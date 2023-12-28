import sys

I = []
P = {}

portals={}

for line in sys.stdin:
    I.append(line)

for y in range(len(I)):
    for x in range(len(I[y])):
        if I[y][x] == '.':
            st=''.join([I[y+1][x], I[y+2][x]])
            if st.isalpha(): portals.setdefault(st, []).append((y,x))
            st=''.join([I[y-2][x], I[y-1][x]])
            if st.isalpha(): portals.setdefault(st, []).append((y,x))
            st=''.join([I[y][x+1], I[y][x+2]])
            if st.isalpha(): portals.setdefault(st, []).append((y,x))
            st=''.join([I[y][x-2], I[y][x-1]])
            if st.isalpha(): portals.setdefault(st, []).append((y,x))

assert len(portals['AA'])==1
assert len(portals['ZZ'])==1
AA=portals.pop('AA')[0]
ZZ=portals.pop('ZZ')[0]

for p in portals.values():
    assert len(p) == 2, '%s'%str(p)
    P[p[0]] = p[1]
    P[p[1]] = p[0]
