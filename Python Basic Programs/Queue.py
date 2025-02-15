l = []
while True:
    option = int(input("1) Enqueue\n2) Dequeue\n3) Front Element\n4) Rear Element\n5) Display\n6) Exit \nEnter an Option Form Above : "))
    
    if option == 1:
        num = input("Enter the Value to Enqueue : ")
        l.append(num)
        print("Element "+ num +" Enqueued successfully to the Enqueue...")
    elif option == 2:
        if len(l) == 0:
            print("Queue is Empty...")
        else :
            n = l.pop()
            print("Element "+ n +" successfully Popped from Queue...")
    elif option == 3:
        if len(l) == 0:
            print("Queue is Empty...")
        else :
            n = l[0]
            print("Front Element of Queue : "+n)
    elif option == 4:
        if len(l) == 0:
            print("Queue is Empty...")
        else :
            n = l[-1]
            print("Rear Element of Queue : "+n)
    elif option == 5:
        if len(l) == 0:
            print("Queue is Empty...")
        else :
            print("Queue Elements : ")
            print(l)
            print("\n")
    else : 
        print("Enter a valid Number...")
        break;