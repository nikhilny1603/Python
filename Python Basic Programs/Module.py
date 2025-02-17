import Function

print(Function.AddNumbers(3,6))

print(Function.Product(3,6))
 
#Second Method

from Function import AddNumbers
from Function import Product
from Function import *
print(AddNumbers(4,8))
print(Product(4,7))

#Third Method Using Alias of Module Function

import Function as f
print(f.sum(12,23))