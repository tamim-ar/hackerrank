from itertools import product

K, M = map(int, input().split())
lists = [list(map(int, input().split()))[1:] for _ in range(K)]

print(max(sum(x**2 for x in combo) % M for combo in product(*lists)))
