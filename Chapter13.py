# 2) write a program to input name, marks and phone number of a student and format it using the format function like below:
#  "The name of the student is harry, his marks are 72 and phone number is 111111111"

name=input("enter name :")
marks=int(input("enter marks :"))
phone=int(input("enter phone number :"))

a="The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone)
print(a)

# 3) A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table=[str(7*i) for i in range(1,11)]
a="\n".join(table)
print(a)  

# 4) write a program to filter a list of numbers which are divisible by 5

l=[5,8,9,10,45,32,85]
a=lambda x:x%5==0
f=filter(a,l)
print(list(f))

# 5) write a program to find the maximum of the numbers in a list using the reduce function

from functools import reduce
l=[1,2,333,4,5]

def greater(a,b):
    if(a>b):
        return a
    return b

r=reduce(greater,l)
print(r) 
