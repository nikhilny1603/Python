class Encapsulation:
    a = 10
    def getter(self):
        return self.a
    
    def setter(self,aa):
        self.a = aa
        
o = Encapsulation()
o.setter(25)
num = o.getter()
print(num)