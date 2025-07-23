student_marks = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eve': 88
}

student_name = input("Enter the student's name: ").strip().title()

marks = student_marks.get(student_name)

if marks is not None:
    print(f"{student_name}'s marks: {marks}")

else:
    print(f"Student '{student_name}' not found.")


