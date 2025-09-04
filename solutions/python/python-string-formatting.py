def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(f"{i:>{width}} {oct(i)[2:]:>{width}} {hex(i)[2:].upper():>{width}} {bin(i)[2:]:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
