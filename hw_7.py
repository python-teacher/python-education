"""
Write a program to count the number of lines in a text file.
"""


def count_rows():
    with open('file/short documentation.txt', 'r') as f:
        line = f.readlines()
        return len(line)


print(count_rows())
