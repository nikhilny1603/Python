str = "Hello World!"

print(str)
print(str[6])

#Slicing 
print(str[0:])
s = len(str)
print(str[:s])
print(str[3:7])
print(str[-1::-1])

#Concatenation
str2 = " I am Learning Python."
print(str + str2)

#String Function
print(str.endswith("!"))
str.capitalize()
print(str)
str.lower()
print(str)
str.upper()
print(str)
print(str.count("l"))
print(str.find('W'))
print(str.replace('llo','poi'))


