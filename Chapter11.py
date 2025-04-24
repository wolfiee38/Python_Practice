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
        
        
