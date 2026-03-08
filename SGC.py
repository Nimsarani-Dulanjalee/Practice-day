# Student Grade Tracker

# 1. Ask for the student's name
name = input("Enter the student's name: ")

# 2. Ask for 3 subject marks
# We convert the input to a float so we can perform calculations
mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

# 3. Calculate the average
average = (mark1 + mark2 + mark3) / 3

# 4. Display the results
print(f"\n--- Results for {name} ---")
print(f"Average Mark: {average:.2f}")

if average >= 40:
    print("Status: Pass")
else:
    print("Status: Fail")
input("\nPress Enter to exit...")