import string
import random

letters = string.ascii_letters

answer = str(random.choice(letters))
print(answer)

turns = 3

for turn in range(turns):
    print("Turn: " + str(turn + 1))
    guess = str(input("Enter your choice from A-Z and a-z: "))
    if guess == answer:
        print("Bravo! You guessed it right...")
        break
    else:
        print("Oops! You guessed it wrong...")
        print("Try again...")
        print()

if guess != answer:
    print("Sorry, you have reached the maximum number of tries")
    print("The answer was: ", answer)
