if __name__ == '__main__':
    n, m = map(int, input().split())
    marks = [list(map(float, input().split())) for _ in range(m)]
    
    # Transpose the marks to group by student
    students_marks = zip(*marks)
    
    # Calculate and print the average for each student
    for student in students_marks:
        print(sum(student) / m)
