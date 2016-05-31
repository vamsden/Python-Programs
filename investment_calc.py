amount = input("Enter your principal amount: ")
rate = input("Enter the rate: ")
time = input("Enter the number of years: ")

amount, rate, time = float(amount), float(rate), int(time)

print("Principal Amount: ", amount)
print("Annual rate of return: ", rate)


def invest(amount, rate, time):
    count = 1
    for x in range(1, int(time) + 1, 1):
        result = amount * (rate + 1) ** count
        print("Year", count, float(result))
        count += 1

invest(amount, rate, time)
