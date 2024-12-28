# Python calculator

operator = input("Enter an operator (+ - */): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))


if operator == "+":
    result = num1+num2
    print(num1, "+", num2, "=", result)
elif operator == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif operator == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif operator == "/":
    result = num1 / num2
    print( num1, "/", num2, "=", result)
else:
    print(f" {operator} is not a valid operation")