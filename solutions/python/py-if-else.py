number = int(input())

if number % 2 != 0:
    print("Weird")
elif number % 2 == 0 and 1 <= number <= 5:
    print("Not Weird")
elif number % 2 == 0 and 6 <= number <= 20:
    print("Weird")
else:
    print("Not Weird")
