from itertools import groupby

S = str(input())
m=[]
l = [list(g) for k, g in groupby(S)]

for i in l:
    t = []
    t.append(len(i))
    t.append(int(i[0]))
    t = tuple(t)
    m.append(str(t))
print (" ".join(m))