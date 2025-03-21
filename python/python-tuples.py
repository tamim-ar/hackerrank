if __name__ == '__main__':
    n = int(input())  # Read the number of elements (not used directly)
    integer_list = tuple(map(int, input().split()))  # Create a tuple from input integers
    print(hash(integer_list))  # Print the hash value of the tuple
