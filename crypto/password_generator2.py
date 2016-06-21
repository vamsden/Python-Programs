import string
import random

def pw_gen(size):
	while size > 8:
		chars = string.ascii_letters + string.digits + string.punctuation
		return ''.join(random.choice(chars) for _ in range(size))
	else:
		return pw_gen(int(input("Password length should be greater than eight: ")))

print("Your new password is: " + str(pw_gen(int(input("Enter the length of your password: ")))))
