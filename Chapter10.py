#1) create a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"
    def __init__(self,name,language,salary):
        self.name=name
        self.language=language
        self.salary=salary
        print(f"The detail is followed {self.name}")
        
    def getinfo(self):
        print(f'the company {self.company}\n name is {self.name}\n language is {self.language} \n salary is {self.salary}')
    
        
harry=Programmer("harry","js",5000)

harry.getinfo()


#2) write a class calculator to find square, cube and square root of a number
import math

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        result = self.n * self.n
        print(f"Square of {self.n} is {result}")

    def cube(self):
        result = self.n * self.n * self.n
        print(f"Cube of {self.n} is {result}")

    def squareroot(self):
        result = math.sqrt(self.n)
        print(f"Square root of {self.n} is {result:.2f}")
a = Calculator(5)
a.square()
a.cube()
a.squareroot()


#3) Use static method and greet user

class greeting:
    
    @staticmethod
    def greet():
        print("hello good eve")
        
a=greeting()
a.greet()


# 4) write program to book train ticket , view status , price
from random import randint
class railway:
    
    def __init__(self,trainno):
        self.trainno=trainno
    
    def booking(self ,to ,fro):
        
        print(f'the journey is between {to} to {fro}')
    
    def status(self,status):
        print(f'the train {self.trainno} is running {status}')
    
    def price(self):
        print(f'the price is {randint(111,2222)}')

hawra=railway(444)
hawra.booking("bhagpur","jaipur")
hawra.status('on time')
hawra.price()

    
