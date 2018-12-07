"""
Write a program to read last n lines of a file.
"""


def read_last_N_lines(n):
    with open('file/short documentation.txt', 'r') as f:
        return f.readlines()[-n:]
print(read_last_N_lines(10))