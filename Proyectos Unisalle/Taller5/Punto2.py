# EXERCISE 2: STANDARD DEVIATION
print("--- STANDARD DEVIATION CALCULATOR ---")

data = []
while True:
    entry = input("Add numbers to calculate desviation (to end list please type 'end'):")
    if entry == "end":
        break
    data.append(float(entry))

# 1. Sum and count
total_sum = sum(data)
total_count = len(data)

# 2. Average
average = total_sum / total_count

# 3. Sum of squares
sum_of_squares = 0
for i in data:
    sub = (i - average)**2
    sum_of_squares += sub

# 4. Result
standard_deviation = (sum_of_squares / total_count)**0.5

print("Dataset:", data)
print("Average (Mean):", average)
print("Sum of Squares:", sum_of_squares)
print("Standard Deviation:", standard_deviation)
