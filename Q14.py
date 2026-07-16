"""
14. Write a program to read the contents of student.txt and

a. Print all content.

Output:
Python is easy to learn.
File handling is important.
Practice makes perfect.

b. Print line-by-line.

Output:
Line 1: Python is easy to learn.
Line 2: File handling is important.
Line 3: Practice makes perfect.
"""

file = open("student.txt", "r")

# a. Print all content
content = file.read()

print("File Content:")
print(content)

file.close()

print()

file = open("student.txt", "r")

# b. Print line by line
line_number = 1

for line in file:
    print("Line", line_number, ":", line.strip())
    line_number = line_number + 1

file.close()