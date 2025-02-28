import json

d = {
    "Name":"Nikhil",
    "Age":20,
    "City":"Ich"
}

f = json.dumps(d)
print(f)
print(type(f))

h = json.loads(d)
print(h)
print(type(h))