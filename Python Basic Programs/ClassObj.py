class DemoClass:
    a = 10
    def Sum(self):
        print(20 + 40)
    
    def Square(self):
        print(self.a*self.a)
        
    def Product(self,a,b):
        print(a*b)
        
ob1 = DemoClass()
print(ob1.a)

ob2 = DemoClass()
print(ob2.a)

ob1.Sum()
ob2.Sum()

ob1.Square()
ob2.Square()

ob1.Product(2,6)
ob2.Product(5,8)