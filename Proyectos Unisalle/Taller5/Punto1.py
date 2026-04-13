# EXERCISE 1: SUM OF ODD NUMBERS
print("--- ODD NUMBER SUMMATION REPORT ---")

n = abs(int(input("Please enter a positive int (N): ")))
# abs() was used to ensure the number is treated as positive
# (Mathematical Absolute Value)

total_sum = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)
        total_sum = total_sum + i

print("The total sum of the odd numbers between 1 and (N) is", total_sum)
