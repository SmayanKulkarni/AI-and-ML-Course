def decimal_to_binary(n, register_size):
    if n < 0:
        return bin(n & ((1 << register_size) - 1))[2:].zfill(register_size)  # Two's complement representation
    else:
        return bin(n)[2:].zfill(register_size)

def binary_to_decimal(b):
    return int(b, 2)

def booth_multiplication(multiplier, multiplicand, register_size):
    # Handle sign of input numbers
    multiplier_sign = -1 if multiplier < 0 else 1
    multiplicand_sign = -1 if multiplicand < 0 else 1

    multiplier = abs(multiplier)
    multiplicand = abs(multiplicand)

    # Binary Conversion
    multiplier_binary = decimal_to_binary(multiplier, register_size)
    multiplicand_binary = decimal_to_binary(multiplicand, register_size)

    product = 0

    print(f"**Step 1: Initialize the registers (each {register_size}-bit)**")
    print(f"P: 0 ({register_size}-bit), M: {multiplier_binary} ({multiplier}) ({register_size}-bit), Q: {multiplicand_binary} ({multiplicand}) ({register_size}-bit)")

    # Multiplication
    multiplier_int = binary_to_decimal(multiplier_binary)
    multiplicand_int = binary_to_decimal(multiplicand_binary)

    steps = []
    for i in range(register_size):
        print(f"**Step {i+2}: Check the least significant bit of M**")
        print(f"M: {decimal_to_binary(multiplier_int, register_size)} ({register_size}-bit), LSB(M): {multiplier_int & 1}")

        if multiplier_int & 1:
            print(f"**Step {i+3}: Add Q to P**")
            product += multiplicand_int
            print(f"P: {product} ({register_size}-bit)")

        print(f"**Step {i+4}: Shift M right by 1 bit**")
        multiplier_int >>= 1
        print(f"M: {decimal_to_binary(multiplier_int, register_size)} ({register_size}-bit)")

        print(f"**Step {i+5}: Shift Q left by 1 bit**")
        multiplicand_int <<= 1
        print(f"Q: {decimal_to_binary(multiplicand_int, register_size)} ({register_size}-bit)")

        steps.append({
            "Step": i+2,
            "M": decimal_to_binary(multiplier_int, register_size),
            "LSB(M)": multiplier_int & 1,
            "P": product,
            "Q": decimal_to_binary(multiplicand_int, register_size)
        })

    print(f"**Step {register_size+2}: The algorithm terminates**")
    print(f"The final product is stored in the product register (P): {product} (decimal) = {decimal_to_binary(product, register_size*2)} (binary) ({register_size*2}-bit)")

    # Apply sign to the result
    result = product * multiplier_sign * multiplicand_sign

    # Print Table
    print("\n**Table View:**")
    print(f"{'Step':<5} | {'M':<20} | {'LSB(M)':<7} | {'P':<20} | {'Q':<20}")
    print('-' * 80)
    for step in steps:
        print(f"{step['Step']:<5} | {step['M']:<20} | {step['LSB(M)']:<7} | {decimal_to_binary(step['P'], register_size*2):<20} | {step['Q']:<20}")
    print()

    return result

register_size = int(input("Enter the register size (in bits): "))
multiplier = int(input("Enter the multiplier (decimal): "))
multiplicand = int(input("Enter the multiplicand (decimal): "))

result = booth_multiplication(multiplier, multiplicand, register_size)
print(f"The product of {multiplier} and {multiplicand} is {result} (decimal) = {decimal_to_binary(result, register_size*2)} (binary) ({register_size*2}-bit)")
