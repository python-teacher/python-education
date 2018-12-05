"""
Write a program to count the number of lines in a text file.
"""


def count_rows():
    with open('documentation file/short documentation.txt', 'r') as f:
        return sum(1 for x in f)


print(count_rows())
