# Variable and data type and Operators

# find addition 
def addition(a,b):
    c=a+b
    print(c)
addition(3,5)

# find remainder 
def findremainder(a,b):
    c=a//b
    print(c)
findremainder(12,5)

# find greater
def diff(a,b):
    if (a <= b):
        print("b is greater")
    elif (b >= a):
        print("a is greater")
    else:
        print("Some error happen")

n=int(input("enter the a"))
m= int(input("enter the b"))
diff(n,m)

# find square of number

def findsquare(a):
    c=a*a
    print("The Square is ", c)
findsquare(n)
# find average of two number
def findaverage(a,b):
    c=(a+b)/2
    print("The average is ", c)
findaverage(n,m)
