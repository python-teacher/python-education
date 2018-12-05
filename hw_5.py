"""
Write a program to read last n lines of a file.
"""


def read_last_N_lines():
    with open('file/file.txt', 'r') as f:
        x = int(input('Введіть скільки останніх рядків відобразити?: '))
        lines = f.readlines()[-x:]
        return lines
print(read_last_N_lines())