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


#
  
