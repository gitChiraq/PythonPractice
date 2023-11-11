print("First Number")
num1 = float(input())

print("Second Number")
num2 = float(input())

print("Pick Operator: + , - , * , / , %")
operator = input()

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

elif operator == "%":
    print(num1 % num2)

else:
    print("Invalid Input")