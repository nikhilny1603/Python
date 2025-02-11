num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")

op = input("Enter the Operator(+,-,*,/) : ")
if (op == "+"):
    print("Addition of Numbers is ",num1 + num2)
elif (op == "-"):
    print("Subtraction of Numbers is ",num1 - num2)
elif (op == "*"):
    print("Multiplication of Numbers is ",num1 * num2)
elif (op == "/"):
    print("Division of Numbers is ",num1 / num2)
else:
    print("Invalid Operator...")