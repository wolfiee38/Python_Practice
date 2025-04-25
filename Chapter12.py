'''1) write a program to open three files 1.txt, 2.txt, 3.txt if any these files are not present,a message
without exiting the program should be printed.'''

try:
  with(open (file1.txt ,"r") as f1,
       open(file2.txt,"r")as f2) 
  print(f1.read())
  print(f2.read())
except Exception as e:
  print(e)
print("Welcome")

# 2) write a program to print third, fifth and seventh element from a list using enumerate function.

l=[1,2,3,4,5,6,7,8,9]
for i , item in enumerate(l):
    if i==3 or i==5 or i==7:
        print(item)

# 3) write a list comprehension to print a list which contains the multiplication table of a user entered number.

n=4
table=[i*n for i in range(1,11)]
print(table)

# 5) store the multiplication tables generated in problem 3 in a file names Tables.txt
n=int(input("enter number :"))
table=[n*i for i in range(1,11)]
with open("Tables.txt","a") as f:
    f.write(f"Table of {n} is {str(table)}\n")
    
