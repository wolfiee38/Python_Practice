# Stone paper scissor game

import random
computer = random.choice([1,2,3])
print("Stone Paper Scissor \n s:stone p:paper scissor:c ")
user=input("Enter value: ")
play={"s":1 , "p":2,"c":3}
revplay={1:"s",2:"p","c":3}
print(f'computer choose {revplay[computer]}')
you=play[user]

if you == computer:
    print("Its draw")
else:
    if computer==1 and you==3:
        print("lose")
    elif computer==2 and you==1:
        print("lose")
    elif computer==3 and you==2:
        print("lose")
    elif computer==1 and you==2:
        print("win")
    elif computer==2 and you==3:
        print("win")
    elif computer==3 and you==1:
        print("win")
    else:
        print("something went wrong")
