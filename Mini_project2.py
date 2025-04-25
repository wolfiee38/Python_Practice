'''we are going to write a program that generates a random number and asks the user to guess it.
If the player's guess is higher than the random number, the program should display "Lower number please!"
If the player's guess is lower than the random number, the program should display "Higher number please!"
If the player's guess is equal to the random number, the program should display the number of guesses the player used to arrive at the number

Hint: Use the random module. '''

import random

n = random.randint(1, 100)
a = -1
attempt = 0

while a != n:
    attempt += 1
    a = int(input("Guess the number: "))
    if a > n:
        print("Lower number please!")
    elif a < n:
        print("Higher number please!")
    else:
        print(f"🎉 Correct! You guessed it in {attempt} attempts.")
