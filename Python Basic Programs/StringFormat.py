str = "Hello Guys, My name is {fname}{lname}.".format(fname = "Nikhil ",lname = "Yadav")
print(str)

str1 = "Hello Guys, My name is {0}{1}.".format("Nikhil","Yadav")
print(str1)

str2 = "Hello Guys, My name is {}{}.".format("Nikhil","Yadav")
print(str2)

str3 = "Hello Guys, {a} and {b} are numbers.".format(a = 10, b = 30)
print(str3)

str4 = "Hello Guys, {a:10} and {b} are numbers".format( a = 10, b = 20)
print(str4)

str4 = "Hello Guys, {a:^10} and {b:<10} are numbers".format( a = 10, b = 20)
print(str4)