from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split()))
    last = float('inf')
    result = "Yes"
    while blocks:
        if blocks[0] >= blocks[-1] and blocks[0] <= last:
            last = blocks.popleft()
        elif blocks[-1] >= blocks[0] and blocks[-1] <= last:
            last = blocks.pop()
        else:
            result = "No"
            break
    print(result)
