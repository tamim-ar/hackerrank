from collections import Counter

if __name__ == '__main__':
    s = input()
    count = Counter(s)
    for char, freq in sorted(count.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(f"{char} {freq}")
