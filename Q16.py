"""
16. Write a Python program to add the below line to the file:

Python file handling becomes simple with practice.
"""

file = open("student.txt", "a")

file.write("\nPython file handling becomes simple with practice.")

file.close()

print("Line added successfully.")