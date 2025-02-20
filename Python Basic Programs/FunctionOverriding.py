class Student:
    def Display(self):
        print("This is Student Class.")
        
class Person(Student):
    def Display(self):
        super().Display()
        print("This is Person Class.")

 
o1 = Person()
o1.Display()