''' program to create file and add text
create file with custom data

str="Hello everyone is my first code"
with open("poem.txt",'w') as file:
    file.write(str)
'''

'''
program to find data in which line

lineno=1
with open("poem.txt") as f:
    c=f.readlines()
    cv=f.read()
lineno=1
for l in c:
    if ("how" in l):
        print("the line is",lineno)
        break
    lineno+=1
else:
    print("wrong")

'''
'''
program to replace sensored data

data="how"
with open("poem.txt","r") as f:
    c= f.read()
    ch=c.replace(data,"#####")
with open("poem.txt","w") as f:
    f.write(ch)
'''
