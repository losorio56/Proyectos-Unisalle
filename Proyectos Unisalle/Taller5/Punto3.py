# EXERCISE 3: CALCULATE POWERS

import math
print("--- POWER CALCULATOR ---")

numbers = []

# Input numbers
while True:
    entry = input("Enter a positive integer (or type 'end' to finish): ")
    if entry == 'end':
        break
    if entry.isdigit() and int(entry) > 0:
        numbers.append(int(entry))
    else:
        print("Please enter a valid positive integer.")

# Process and display results

for num in numbers:
    square_root = math.sqrt(num)
    square = num ** 2
    cube = num ** 3
    
    print("Number:", num)
    print("Square Root:", round(square_root, 2))
