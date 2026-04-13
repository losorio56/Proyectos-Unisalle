# EXERCISE 9:NUMERIC BASE CONVERSION

print("decimal number")


def convert_decimal_to_base(decimal_number, target_base):
    if target_base < 2 or target_base > 16:
        return "Error: base must be between 2 and 16."

    digits = "0123456789ABCDEF"
    result = ""

    quotient = decimal_number
    while quotient > 0:
        remainder = quotient % target_base
        quotient = quotient // target_base
        result = digits[remainder] + result

    return result


decimal_number = int(input("Enter a decimal number: "))
target_base = int(input("Enter the target base (between 2 and 16): "))


converted = convert_decimal_to_base(decimal_number, target_base)
print(f"The number in base {target_base} is: {converted}")
