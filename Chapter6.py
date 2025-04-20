#If elif else

# check whether the username is more than 10 letter
n="rudrapratap"
if (len(n) < 10):
    print("not accepted")
else:
    print("acceptedd")

# program to find whether the thing is present in list or not
l=[11,33,1,5,7,2,6,8]
n=int(input("enter the number to find : "))
if n in l:
    print("it present")
else:
    print("not presnet")

#write the grade according to it

n=75
if 90 <= n <= 100:
    print("0")
elif 70 <= n <= 90:
    print("A")
elif 50 <= n <= 70:
    print("B")
else:
    print("fail")



# program for taking n subject where miniumu criteria for eaach subject is 40% and total marks will be 33% and then show pass
n = int(input("Number of subjects: "))
t = []
k = 0
passed_all_subjects = True  # Assume passed unless we find otherwise

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    t.append(m)
    k += m
    if m < 40:
        passed_all_subjects = False  # Failed in this subject

avr = k / len(t)

if passed_all_subjects and avr >= 33:
    print("✅ Passed")
else:
    print("❌ Failed")

print("Total Marks:", k)
print("Average Percentage:", avr)
