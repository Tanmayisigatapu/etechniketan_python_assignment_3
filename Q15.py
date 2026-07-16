"""
15. Write a Python program to count how many words are present in student.txt.

Output:
Total words: 12
"""

file = open("student.txt", "r")

content = file.read()

words = content.split()

print("Total words:", len(words))

file.close()
