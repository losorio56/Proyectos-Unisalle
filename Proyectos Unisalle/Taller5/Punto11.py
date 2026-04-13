# EXERCISE 11:GRADES ANALYSIS

print("grade for student")

N = int(input("Enter the number of students: "))

grades = []
sum_grades = 0
passed = 0
failed = 0

for i in range(1, N + 1):
    grade = float(input(f"Enter grade for student {i}: "))
    grades.append(grade)
    sum_grades += grade

    if grade >= 60:
        passed += 1
    else:
        failed += 1

average = sum_grades / N

highest = max(grades)
lowest = min(grades)

print("\n--- Results ---")
print("Average grade:", average)
print("Number of students passed:", passed)
print("Number of students failed:", failed)
print("Highest grade:", highest)
print("Lowest grade:", lowest)
