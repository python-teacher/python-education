"""
Write a program to count the number of lines in a text file.
"""


def count_rows():
    with open('file/file.txt', 'r') as f:
        count = 0
        for x in f.readlines():
            count += 1
        print('Rows {}'.format(count))


count_rows()
