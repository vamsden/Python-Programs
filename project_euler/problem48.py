total = 0

for i in range(1, 1001):
    num = i ** i
    total = total + num
    series_length = len(str(total))

total = str(total)
lst_10_digit = total[series_length - 10:series_length]

print("Last 10 digits of the series are: ", lst_10_digit)
