# dictionary{a:b} and set={} set()

# english to hindi
dic={"tum":"you","teri":"your"}
print(dic)
print(dic.keys())
print(dic["tum"])
print(dic.items())
print(dic,type(dic))

# Create a set to store student names
s = set()
for i in range(4):
    st = input("Enter name: ")
    s.add(st)
print("Student set:", s,len(s))

# can we have a set with 18(int) and '18' (str) as a value in it?
b=set()
b.add(18)
b.add("18")
print(b)






v={}
name=input("enter name :")
lang=input("enter language :")
v.update({name:lang})
name=input("enter name :")
lang=input("enter language :")
v.update({name:lang})
print(v)


# Ask name and prefer language to 4 student and store in dictionary
fav_lang = {}
for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite language: ")
    fav_lang[name] = language  # Add to dictionary
print("\nFavorite languages dictionary:")
print(fav_lang)
