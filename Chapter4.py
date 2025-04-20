# List[] and tuple()

# program to  store n number of fruit in list and tuple
n = int(input("Number of Fruits : "))
fruit=[]
for i in range(n):
    f = input("Enter the fruit : ")
    fruit.append(f)
print(fruit)
fruit_tuple = tuple(fruit)
print(fruit_tuple)


#create program to accept the marks of student and sort it plus also show it sum

def student(n):
    tmark=[]
    for i in range(n):
        mark=int(input("enter your marks: "))
        tmark.append(mark)
    print(tmark)
    tmark.sort()
    print(tmark)
    smark=sum(tmark)
    print(smark)
n=int(input("enter the num :"))
student(n)

#program to count number of 0 in tuple
t=(2,46,9,0,77,0,77,0)
n=t.count(0)
print(n)
