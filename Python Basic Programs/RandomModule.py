import random as r

print(r.randint(1,100))

print(r.randrange(1,99))

l = [1,2,3,4,5,6,7,8,9]
print(r.choice(l))

print(r.random())

r.shuffle(l)
print(l)

u = r.uniform(2,8)
print(u)