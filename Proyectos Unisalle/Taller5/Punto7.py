# EXERCISE 7: --- FUMIGATION INVOICE ---
print("Fumigation Invoice Calculator")

name = input("Enter the farmer's name: ")
type_of_fumigation = int(input("Enter the type of fumigation (1, 2, 3 or 4):"))
hectares = float(input("Enter the number of hectares to fumigate: "))

if type_of_fumigation == 1:
    price = 10
elif type_of_fumigation == 2:
    price = 15
elif type_of_fumigation == 3:
    price = 20
elif type_of_fumigation == 4:
    price = 30
else:
    print("Invalid fumigation type")
    exit()

total_cost = hectares * price

# discount for large surface
if hectares > 1000:
    total_cost *= 0.95  # 5% of discount

# discount for amount exceeding $3000
if total_cost > 3000:
    excess = total_cost - 3000
    excess_discount = excess * 0.10
    total_cost -= excess_discount


print("--- FUMIGATION INVOICE ---")
print("Farmer: ", name)
print("Total to pay: ", total_cost)
