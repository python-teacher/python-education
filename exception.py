"""
Define your custom class for exceptions. Show an example how it might be used.
"""


class Error(Exception):
    pass


class OtherTypeError(Error):
    pass


class DivideByZero(Error):
    pass


def zero(a, b):
    try:
        if isinstance(a, str) or isinstance(b, str):
            raise OtherTypeError('Invalid type')
        elif int(b) == 0:
            raise DivideByZero('Division by zero')
        else:
            print("{} / {} = {}".format(a, b, (a / b)))
    except OtherTypeError as ddt:
        print(ddt)
    except DivideByZero as dz:
        print(dz)


zero(5, 5)
zero('5', 5)
zero(5, '0')
zero(5, 0)
zero(0, 1023)
zero(555, 'budz')
