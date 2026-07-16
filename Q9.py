"""
9. WAP to create a function drop_minimum that takes variable length arguments (*args).

The function takes integers and returns a list of these integers after removing
the minimum value from the arguments.

Example:
drop_minimum(5, -2, 8, 4, -5, 7, 10)

Output:
[5, -2, 8, 4, 7, 10]
"""

def drop_minimum(*args):

    numbers = list(args)

    minimum = min(numbers)

    numbers.remove(minimum)

    return numbers

result = drop_minimum(5, -2, 8, 4, -5, 7, 10)

print(result)