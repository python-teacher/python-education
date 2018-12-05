"""
Write a program to find the longest word in the file.
"""


def long_word():
    with open('documentation file/short documentation.txt', 'r') as f:
        read_file = f.read()
        split_on_words = read_file.split()
        return max(split_on_words, key=len)


print(long_word())