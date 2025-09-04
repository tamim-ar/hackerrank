from collections import deque
d = deque()
for _ in range(int(input())):
    cmd = input().split()
    getattr(d, cmd[0])(*[cmd[1]] if len(cmd) > 1 else [])
print(*d)
