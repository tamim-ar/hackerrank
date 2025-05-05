from collections import namedtuple
n = int(input())
fields = input().split()
Student = namedtuple('Student', fields)
print("{:.2f}".format(sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n))
