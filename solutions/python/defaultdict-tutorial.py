from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)

for i in range(1, n + 1):
    word = input()
    d[word].append(i)

for _ in range(m):
    query = input()
    if query in d:
        print(*d[query])
    else:
        print(-1)
