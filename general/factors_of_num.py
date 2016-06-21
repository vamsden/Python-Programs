x = int(input("Enter a number: "))


def factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, "is a divisor of", str(x))

factors(x)
