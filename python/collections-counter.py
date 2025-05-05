from collections import Counter

_ = int(input())
shoe_sizes = Counter(map(int, input().split()))
total = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        total += price
        shoe_sizes[size] -= 1

print(total)
