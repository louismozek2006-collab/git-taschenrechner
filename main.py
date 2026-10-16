print("=== My calculator ===")

n1 = float(input("Enter first number: "))
op = input("Arithmetic operation (+, -, *, /): ")
n2 = float(input("Enter second number: "))

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    if n2 != 0:
        result = n1 / n2
    else:
        result = None
        print("Error: division by zero is undefined.")
else:
    result = None
    print("Unknown arithmetic operation.")

if result is not None:
    print("Result:", result)