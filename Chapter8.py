# function and recursion
# print n sum of natural number
def nsum(n):
    if n==0:
        return 0
    return n+ nsum(n-1)
print(nsum(3))

#factorial 
def nsum(n):
    if n==1:
        return 1
    return n* nsum(n-1)
print(nsum(4))

# Star function
def nsum(n):
    if n==0:
        print("")
    print("*"*n)
    nsum(n-1)
print(nsum(5))
