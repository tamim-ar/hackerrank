from itertools import combinations_with_replacement

s, k = input().split()
for combo in combinations_with_replacement(sorted(s), int(k)):
    print(''.join(combo))
