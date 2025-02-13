l = []
while True:
    option = int(input("1) Push Element\n2) Pop Element\n3) Peek Element\n4) Display\n5)Exit\nPlease Enter an Option form Above : "))
    
    if option == 1:
        num = input("Enter the Value to Push : ")
        l.append(num)
        print("Element "+ num +" added successfully to the Stack...")
    elif option == 2:
        if len(l) == 0:
            print("Stack is Empty...")
        else:
            p = l.pop()
            print("Element "+ p +" popped successfully from the Stack...")
    elif option == 3:
        if len(l) == 0:
            print("Stack is Empty...")
        else:
            print("Peek Element of the Stack is "+l[-1])
    elif option == 4:
        if len(l) == 0:
            print("Stack is Empty...")
        else:
            print("Element of the Stack :\n")
            print(l)
    else:
        print("Enter a valid number...")
        break;