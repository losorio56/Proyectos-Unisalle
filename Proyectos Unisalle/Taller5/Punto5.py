# EXERCISE 5:DETECTION OF RIGHT TRIANGLES
print(" TRIPLETS OF NUMBERS")

def count_right_triangles(triples):
    counter = 0

    for triple in triples:
        a, b, c = triple

        # Identify the largest side as hypotenuse
        if a >= b and a >= c:
            hypotenuse, side1, side2 = a, b, c
        elif b >= a and b >= c:
            hypotenuse, side1, side2 = b, a, c
        else:
            hypotenuse, side1, side2 = c, a, b

        # Check Pythagoras' theorem
        if hypotenuse**2 == side1**2 + side2**2:
            counter += 1

    return counter

# Example usage
N = int(input("Enter the number of triples: "))
triples = []

for i in range(N):
    print(f"Triple {i+1}:")
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    triples.append((a, b, c))

result = count_right_triangles(triples)
print("Number of triples that form right triangles:", result)
