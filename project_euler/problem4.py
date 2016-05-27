"""
Problem 4:

Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome_list = []

for x in range(100, 1000):
    for y in range(100, 1000):
        number = str(x * y)
        rev_number = number[::-1]
        if number == rev_number:
            palindrome_list.append(int(number))

print("The Largest palindrome of product of 3 digit number is: " +
      str(max(palindrome_list)))
