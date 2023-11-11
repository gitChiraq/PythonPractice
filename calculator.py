print("First Number")
num1 = input()

def is_float(string):
    try: 
        float(string)
        return True
    except ValueError:
        return False

while is_float(num1) is False:
    print("Invalid input")
    print("First Number")
    num1 = input()

print(float(num1))

print("Second Number")
num2 = float(input())

while is_float(num2) is False:
    print("Invalid input")
    print("First Number")
    num1 = input()

print("Pick Operator: + , - , * , / , %")
operator = input()
while True:
    if operator == "+":
        print(float(num1) + float(num2))
        break

    elif operator == "-":
        print(float(num1) - float(num2))
        break

    elif operator == "*":
        print(float(num1) * float(num2))
        break

    elif operator == "/":
        print(float(num1) / float(num2))
        break

    elif operator == "%":
        print(float(num1) % float(num2))
        break

    else:
        print("Invalid Input")
        print("Pick Operator: + , - , * , / , %")
        operator = input()