def celsius_to_fahrenheit(celsius):
    fahrenheit = float(celsius) * 9 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (float(fahrenheit) - 32) * 5 / 9
    return celsius


while True:
    x = input("Convert to celsius or fahrenheit. Input c or f ").lower()
    if x == str("c"):
        fahrenheit = input("Enter temperature in fahrenheit: ")
        print(str(fahrenheit) + " degrees F = " + " " +
              str(fahrenheit_to_celsius(fahrenheit)) + " degrees C")
        break
    elif x == str("f"):
        celsius = input("Enter temperature in celsius ")
        print(str(celsius) + " degrees C = " + " " +
              str(celsius_to_fahrenheit(celsius)) + "degrees F")
        break
    else:
        print("Incorrect input")
