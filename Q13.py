"""
13. Write a Python program to create a file called student.txt.
Write the following three lines into it:

Python is easy to learn.
File handling is important.
Practice makes perfect.

Use exception/error handling to catch FileExistsError
and all other errors (Exception).
"""

try:
    file = open("student.txt", "x")

    file.write("Python is easy to learn.\n")
    file.write("File handling is important.\n")
    file.write("Practice makes perfect.")

    file.close()

    print("File created successfully.")

except FileExistsError:
    print("File already exists.")

except Exception as e:
    print("Error:", e)