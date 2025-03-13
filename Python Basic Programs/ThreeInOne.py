#first program
print(" +  program first")

marks = int(input("Enter the marks of the student: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
else:
    print("FAIL")

    #second program
    print("second program")

def check_number_type(number):
    if number <= 1:
        return "Neither prime nor composite"
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return "Composite"
    return "Prime"
num = int(input("Enter a number: "))
result = check_number_type(num)
print(f"The number {num} is {result}.")

#third program
print("thrird program")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")    