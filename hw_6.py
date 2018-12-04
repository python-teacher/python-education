"""
Write a program to find the longest word in the file.
"""


def long_word():
    with open('file/file.txt', 'r') as f:
        print(max(f.read().split(), key=len))


long_word()
