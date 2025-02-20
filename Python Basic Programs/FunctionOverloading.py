class Demo:
    def Area(self,a=None,b=None):
        
        if a!= None and b!=None:
            print("Area of Rectangle is "+str(a*b))
        elif a!=None:
            print("Area of Square is "+str(a*a))
        else:
            print("Invalid")
        
    
o = Demo()
o.Area()
o.Area(4)
o.Area(5,4)

