# generate a password with length "passlen" with no duplicate characters in the password

import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password_length = int(input("Enter the length of the password: "))

password =  "".join(random.sample(characters, password_length))
print("New generated password is: " + password)
