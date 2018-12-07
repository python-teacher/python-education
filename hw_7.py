"""
Write a program to count the number of lines in a text file.
"""


def count_rows():
    return len(open('file/short documentation.txt', 'r').readlines())


print(count_rows())
