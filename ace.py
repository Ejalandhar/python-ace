
def calculate_grade(total_score):
    if total_score >= 90:
        return 'A'
    elif total_score >= 80:
        return 'B'
    elif total_score >= 70:
        return 'C'
    elif total_score >= 60:
        return 'D'
    else:
        return 'F'
def display_students(student_list):
    print("\nStudent Details:")
    for student in student_list:
        print(f"Name: {student['name']}, Student ID: {student['student_id']}, Total Score: {student['total_score']}, Grade: {student['grade']}")
def student_grade_management():
    students = []
    while True:
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        scores = []
        for i in range(1, 4):
            score = int(input(f"Enter score for subject {i}: "))
            scores.append(score)
        total_score = sum(scores)
        grade = calculate_grade(total_score)
        student = {
            'name': name,
            'student_id': student_id,
            'total_score': total_score,
            'grade': grade
        }
        students.append(student)
        more_students = input("Do you want to add another student? (yes/no): ")
        if more_students.lower() != 'yes':
            break

    display_students(students)
student_grade_management()
