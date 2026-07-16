"""
8. WAP to create a function named 'introduce' that takes 2 arguments:
a. name – positional argument
b. age – default argument with a default value of None.

If age is provided while calling the function,
introduce("John", 20), print =>
My name is John. I am 20 years old.

If age is not provided while calling the function,
introduce("John"), print =>
My name is John. My age is secret.
"""

def introduce(name, age=None):

    if age == None:
        print("My name is", name + ".")
        print("My age is secret.")
    else:
        print("My name is", name + ".")
        print("I am", age, "years old.")

introduce("John", 20)

introduce("John")