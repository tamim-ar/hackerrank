# Reading input
n, m = map(int, input().split())  # n: number of athletes, m: number of attributes
arr = [list(map(int, input().split())) for _ in range(n)]  # Athlete data (n rows)
k = int(input())  # The index of the attribute to sort by

# Sort the list by the k-th attribute
arr.sort(key=lambda x: x[k])

# Print the sorted table
for athlete in arr:
    print(" ".join(map(str, athlete)))
