"""
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def findLargestPrimeFactor(n):
    primeFactor = 1
    i = 2

    while i <= n / i:
        if n % i == 0:
            primeFactor = i
            n /= i
        else:
            i += 1

    if primeFactor < n:
        primeFactor = n

    return primeFactor

print("The largest Prime Factor of 600851475143 is :", findLargestPrimeFactor(600851475143))


"""
def prime_fact(num):
    for i in range(2, num):
        if (num % i) == 0 and (num % 1) == 0:
            print(i)

prime_fact(13195)
"""
