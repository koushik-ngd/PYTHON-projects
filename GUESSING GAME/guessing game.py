
import random

n = random.randint(0,100)

#print(n) # if you remove the option to print the n value then you should guess the number without knowing 

guess = int(input("Enter a number from 1 - 100:"))

while n != guess:
    if guess < n:
        print("The guessed number is lower than the actual number. Try again!")
        guess = int(input("Enter a number from 1 - 100:"))
        
    elif guess > n:
        print("The guessed number is greater than the actual number. Try again!")
        guess = int(input("Enter a number from 1 - 100:"))
        
while n == guess:
        print("You guessed it right")
        break

