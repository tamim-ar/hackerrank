# Reading the input values
x, expected_value = map(int, input().split())
polynomial = input()

# Evaluating the polynomial expression
result = eval(polynomial)

# Check if the evaluated result matches the expected value
if result == expected_value:
    print(True)
else:
    print(False)
