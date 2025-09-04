class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        num = self.current
        self.current += 2
        return num

class OddStream:
    def __init__(self):
        self.current = 1

    def get_next(self):
        num = self.current
        self.current += 2
        return num

def print_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        stream_name, n = input().split()
        n = int(n)
        if stream_name == 'even':
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())
