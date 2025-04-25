#Inherhitance (Single , Multiple , Multilevel)
# Super, classmethod, getter, setter , property , class operator

# 1) create a class(2-D vector) and use it to create another class representing 3-D vector

class V2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The value of i and j is  {self.i} and {self.j}")
        
class V3D(V2D):  # Single Level Inheritance
    def __init__(self,i,j,k):
        self.k=k
        super().__init__(i,j)
    def dshow(self):
        print(f"the i = {self.i},j={self.j},k={self.k}")
a=V3D(1,2,3)
a.dshow()
a.show()
        
# 2) create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 'Pets'. Add a method 'bark' to 'Dog' class.

# Multi-Level Inheritance
class Animal:
    pass
class Pets(Animal):
    pass
class Dog(Pets):
    @staticmethod  #self nhi daalne ke liye
    def bark():
        print("Dog barks on elephant")
        
a=Dog()
a.bark()

'''3) create a class 'Employee' and add salary and increment properties to it. Write a method 'salaryAfterIncrement' method
with a @property decorator with a setter which changes the value of increment based on the salary'''

class employee:
    salary=234
    increment=20
    
    @property
    def salaryafteincrement(self):
        return ((self.salary) + (self.salary * (self.increment/100)))
        
    @salaryafteincrement.setter
    def salaryafteincrement(self , salary):
        self.increment = ((salary/self.salary) -1) *100
        
    
a=employee()
print(a.salaryafteincrement)
a.salaryafteincrement=300
print(a.salaryafteincrement)

# 4) write a class 'Complex' to represent complex numbers, along with overloaded operators '+' and '*' which adds and multiplies them

class complex:
    def __init__(self , r ,i):
        self.r=r
        self.i=i
    
    def __add__(self,c2):
        return complex(self.r + c2.r, self.i + c2.i)
    
    def __str__(self):
        return f"{self.r} + {self.i}"
       
        
a=complex(11,22)
b=complex(33,11)
print(a+b)

# 7) Override the __len_() method on vector of question 5 to display the dimension of the vector

class vector:
    def __init__(self,l):
        self.l=l
        
    def __len__(self):
        return len(self.l)
v=vector([1,4,2])
print(len(v))
    
# 6) write __str__() method to print the vector 7i + 8j + 10k

class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
v=vector(7,8,10)
print(v)

        
