# EXERCISE 6: Employee Payroll Optimization
print("--- Employee Payroll Optimization Program ---")


while True:
    name = input("Type employee name (or 'done' to finish): ")
    if name == "done":
        print("Program finished")
        break

    children = int(input("Type number of children: "))
    hours_worked = float(input("Type hours worked in the month: "))
    hourly_rate = float(input("Type hourly rate: "))

    salary = hours_worked * hourly_rate

    # Retention
    if salary < 300000:
        if children > 6:
            retention = 0
        else:
            percentage = (6 - children) / 2
            retention = salary * percentage / 100
    else:
        if children < 3:
            retention = salary * 0.03
        else:
            percentage = 10 / children
            retention = salary * percentage / 100

    subsidy = children * 1200
    total = salary - retention + subsidy

    print("---- Salary Report for", name, "----")
    print("Gross Salary", salary)
    print("Retention:", retention)
    print("Subsidy:", subsidy)
    print("Total to pay:", total)
