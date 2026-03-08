# Student Grade Tracker v3.0

# 1. Inputs
name = input("Enter the student's name: ")
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

# 2. Calculation
average = (mark1 + mark2 + mark3) / 3

# 3. Grading Logic
if average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

# 4. Formatted Output
print("-" * 30)
print(f"Name   : {name}")
print(f"Average: {average:.1f}")
print(f"Grade  : {grade}")
print("-" * 27)
input("Press Enter to exit...")