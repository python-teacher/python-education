"""
Write a program to find the longest word in the file.
"""


def long_word():
    with open('file/other text.txt', 'r') as f:
        read_file = f.read()
        words = read_file.split()
        return max(words, key=len)


print(long_word())