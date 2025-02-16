 d = {
     "Name": "Nikhil",
     "Age" : 20,
     "PRN" : "22UAI133",
     "City": "Ichalkaranji"
 }

 print(d)
 print(type(d))

 for e in d:
     print(d[e])
    
 print(d["Name"])
 print(d["Age"])

 #Dictionary Functions

 print(d.keys())
 print(d.values())
 print(d.items())
 print(d.get('Name'))
 d.update({"CGPA": 8.7}) 
 print(d)
 del d["City"]
 print(d)
 d["Course"] = "Python"
 print(d)

#Nested Dicitonary

dict = {
    "Java":{"dur":"3m","fee":"5000"},
    "Python":{"dur":"2m","fee":"8000"},
    "JavaScript":{"dur":"1.5m","fee":"4000"},
}
print(dict)
print(dict['Java'])
print(dict['Python']['fee'])

for a,b in dict.items():
    print(a,b['dur'],b['fee'])
    
dict["Java"]['dur'] = "5m"
print(dict)
    
