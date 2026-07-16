"""
10. A function find_max(a, b, c) that returns the largest of its three arguments
by calling the built-in max() function.

Create another function called main() that reads three user inputs
x, y & z from the user (integers) and calls find_max() function.

The main() function should print only the resulting maximum value.
"""

def find_max(a, b, c):
    return max(a, b, c)

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    z = int(input("Enter third number: "))

    print(find_max(x, y, z))

main()