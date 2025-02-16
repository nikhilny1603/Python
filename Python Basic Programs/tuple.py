t = (10,20,30,40,50,60)

print(t)

a = t[1]
print(a)

for a in range(len(t)):
    print(t[a])
    
# tuple functions
m = max(t)
print(m)
print(min(t))
print(t.count(20))
print(t.index(30))
print(sum(t))

#tuple Slicing

print(t[:len(t)])
print(t[0:])
print(t[1:4])
