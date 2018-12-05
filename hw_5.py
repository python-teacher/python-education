"""
Write a program to read last n lines of a file.
"""


def read_last_N_lines():
    with open('file/short documentation.txt', 'r') as f:
        return f.readlines()[-5:]
print(read_last_N_lines())