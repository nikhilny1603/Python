s = {10,20,30,40,50,60,70}

print(s)

for a in s:
    print(a)
    
s1 = {1,2,3,1,4,3,2,5,4,3,2}
print(s1)

#set Functions
L = [1,2,3,4,5]
s = set(L)
print(s)

s1.add(45)
print(s1) 

print(s1.pop())
s1.pop()
print(s1)

s1.remove(45)
print(s1)

s1.discard(3)
print(s1)

s1.clear()
print(s1)

s1.update(L)
print(s1)

