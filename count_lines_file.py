"""
Write a program to count the number of lines in a text file.
"""


def count_rows():
    with open('testing_data.txt', 'r') as f:
        lines = f.readlines()
        return len(lines)


print(count_rows())
