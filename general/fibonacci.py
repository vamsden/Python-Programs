user_input = int(input("Enter the length of the series: "))


def fibonacci(length):
    count = 2
    series = [0, 1]
    while count < length:
        result = series[len(series)-1] + series[len(series)-2]
        series.append(result)
        length -= 1
    print(series)

print("The fibonacci series is of length " + str(user_input) + " is: ")
fibonacci(user_input)
