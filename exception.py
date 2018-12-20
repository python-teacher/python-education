"""
Define your custom class for exceptions. Show an example how it might be used.
"""


class Calculator:
    def zero(a, b):
        try:
            print("{} / {} = {}".format(a, b, (a / b)))
        except (ZeroDivisionError, ValueError, TypeError):
            print("{} / {} = {}".format(a, b, False))


one = Calculator
one.zero(5, 1)
one.zero(0, 21)
one.zero(312, 0)
one.zero(12, 'bdz1')
