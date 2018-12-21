"""
Define your custom class for exceptions. Show an example how it might be used.
"""


class Error(Exception):
    pass


class Type(Error):
    pass


class ZeroDivision(Error):
    pass


def zero(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            raise Type
        elif int(b) == 0:
            raise ZeroDivision
        else:
            print("{} / {} = {}".format(a, b, (a / b)))
    except Type:
        print('Invalid type')
    except ZeroDivision:
        print('Division by zero')


zero(5, 5)
zero('5', 5)
zero(5, '0')
zero(5, 0)
zero(0, 1023)
zero(555, 'budz')
