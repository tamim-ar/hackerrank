from itertools import combinations

s, k = input().split()
s = sorted(s)
k = int(k)

for i in range(1, k + 1):
    for combo in combinations(s, i):
        print(''.join(combo))
