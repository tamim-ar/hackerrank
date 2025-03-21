if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # Find the second lowest grade
    scores = sorted(set(score for name, score in students))
    second_lowest = scores[1]

    # Collect names of students with the second lowest grade
    result = sorted([name for name, score in students if score == second_lowest])

    # Print each name on a new line
    for name in result:
        print(name)
