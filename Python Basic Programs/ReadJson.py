import json

file = open("Sample.json",'r')
x = file.read()

Data = json.loads(x)

print(Data)
for a in Data:
    print(Data)