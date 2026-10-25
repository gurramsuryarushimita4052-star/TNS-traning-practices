#Student Report Card
# List to store student name
student_names = []

# Set to store subjects
subjects = set()

# Enter student name
name = input("Enter student name: ")
student_names.append(name)

# Enter age
age = int(input("Enter age: "))

# Store student information in tuple
student_info = (name, age)

# Enter number of subjects
n = int(input("Enter no of subjects: "))

# Dictionary to store subject and marks
marks = {}

# Enter subject name and marks
for i in range(n):
    subject = input("Enter subject name: ")
    mark = int(input("Enter subject marks: "))

    subjects.add(subject)
    marks[subject] = mark

# Calculate total marks
total_marks = sum(marks.values())

# Calculate average
average = total_marks / n

# Display report card
print("\n----- REPORT CARD -----")
print("Name:", student_info[0])
print("Age:", student_info[1])
print("Subjects:", subjects)
print("Marks:", marks)
print("Total Marks:", total_marks)
print("Average Marks:", average)
