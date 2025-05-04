if __name__ == '__main__':
    n, m = map(int, input().split())
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    print('\n'.join(pattern))
    print('WELCOME'.center(m, '-'))
    print('\n'.join(pattern[::-1]))
