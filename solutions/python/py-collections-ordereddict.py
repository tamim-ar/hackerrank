from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    *item, price = input().split()
    name = ' '.join(item)
    d[name] = d.get(name, 0) + int(price)
for k, v in d.items():
    print(k, v)
