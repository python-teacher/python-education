"""
Define your custom class for exceptions. Show an example how it might be used.
"""

class Calculator:
    while True:
        try:
            a = int(input('a = '))
            b = int(input('b = '))
            print("{} / {} = {}".format(a,b,(a/b)))
        except (ZeroDivisionError, ValueError):
            print(False)
