import math

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /, ^, sqrt): ")

# if operation == '+':
#     result = a + b
#     print(f"The result of {a} + {b} is: {result}")


#rewriting to encorporate lists in addition
while True:
    a = input("Enter your input: ")

    try:
        parts = a.split("+")
        result = sum(int(part) for part in parts)
        print(f"The result of {a} is: {result}")
        break

    except ValueError:
        print("Invalid input")



