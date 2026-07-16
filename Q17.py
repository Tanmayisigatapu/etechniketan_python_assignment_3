"""
17. Create a list, numbers = [7, 4, 0, -2, 3]. Print this list.
Then ask the user to provide an index for which they want the value.
Use exception handling to handle IndexError.
"""

numbers = [7, 4, 0, -2, 3]

print("List:", numbers)

try:
    index = int(input("Enter the index: "))
    print("Value:", numbers[index])

except IndexError:
    print("Invalid index! Index is out of range.")