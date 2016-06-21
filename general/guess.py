import math
import random


num = random.randint(0, 100)

while True:
	user_input = int(input("Enter you guess: "))
	if user_input < num:
		print("Guess higher!")
	elif user_input > num:
		print("Guess lower!")
	else:
		print("Congrats!")
		break