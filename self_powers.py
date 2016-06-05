"""
Program to print last 10 digits of sequence
1^1 + 2^2 + 3^3 + 4^4 + ..... + 999^999 + 1000^1000 = sum
"""

x = 0
for i in range(1, 1001):
    i_powered = i ** i
    x = x + i_powered

print(len(str(x)))

y = str(x)  # sequence
print("The last 10 digits are: ")
print(y[len(str(x)) - 10: len(str(x))])
