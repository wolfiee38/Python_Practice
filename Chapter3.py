#String 

#display user entered name with good morning
n=input("enter your name : ")
a="good morning " + n
print(a)

# dear name you got selected time
import time
letter= f'Dear {n} you got selected {time.ctime()}'
print(letter)


# fix double space
def fixspaces(inputtext):
    while "  " in inputtext:
        inputtext = inputtext.replace("  ", " ")
    return inputtext

txt = "Thell    hello with  th  "
print("Initial text:", txt)
cleaned = fixspaces(txt)
print("Fixed text:", cleaned)


# format sentence
def format_sentence():
    # A sentence formatted using escape characters
    formatted = "Hello,\n\tWelcome to Python Programming!\n\tLet\'s learn how to use escape sequences:\n"
    formatted += "\t1. New Line -> \\n\n"
    formatted += "\t2. Tab Space -> \\t\n"
    formatted += "\t3. Backslash -> \\\\\n"
    formatted += "\t4. Double Quotes -> \\\"This is in quotes\\\"\n"
    
    print(formatted)

# Call the function
format_sentence()

