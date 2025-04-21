#loop for while 
#table
i=5
l=1
while l <= 10:
    o=i*l
    l+=1
    print(o)

#prime number
n=17
for i in range(2,int(n**0.5)+1):
    prime=False
    if n%2 == 0:
        prime=False
    else:
        prime=True
if prime:
    print("Prime")
else:
    print("not")


#Star qts
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))

print("")

for i in range(1,n+1):
    print("*"*(i))

print("")

i=1
while i<=n:
    if (i==1) or (i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
    i+=1
 
  
