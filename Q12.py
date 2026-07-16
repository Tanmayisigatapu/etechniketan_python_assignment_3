"""
12. Write a lambda function that accepts a temperature in Celsius
(a float number), converts it to the Fahrenheit scale using the formula:

Fahrenheit = Celsius * 9 / 5 + 32
"""

fahrenheit = lambda c: (c * 9 / 5) + 32

celsius = float(input("Enter temperature in Celsius: "))

print("Temperature in Fahrenheit:", fahrenheit(celsius))