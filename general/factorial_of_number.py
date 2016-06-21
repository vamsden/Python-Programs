x = input("Enter your number: ")


def factorial(x):
    fact = 1
    if int(x) == 0:
        return fact
    else:
        while(x != 0):
            fact = fact * int(x)
            x = int(x) - 1
        return fact

print("Factorial of " + str(x) + " is: " + str(factorial(x)))
