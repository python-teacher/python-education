"""
Define your custom class for exceptions. Show an example how it might be used.
"""


class Error(Exception):
    pass


class TypeError(Error):
    pass


class ZeroDivisionError(Error):
    pass


def zero(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError
        elif int(b) == 0:
            raise ZeroDivisionError
        else:
            print("{} / {} = {}".format(a, b, (a / b)))
    except TypeError:
        print('Invalid type')
    except ZeroDivisionError:
        print('Division by zero')


zero(5, 5)
zero('5', 5)
zero(5, '0')
zero(5, 0)
zero(0, 1023)
zero(555, 'budz')
