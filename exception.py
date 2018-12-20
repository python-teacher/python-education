"""
Define your custom class for exceptions. Show an example how it might be used.
"""


class Calculator:
    def zero(a, b):
        try:
            print("{} / {} = {}".format(a, b, (a / b)))
        except (ZeroDivisionError, ValueError, TypeError):
            print("Invalid type or division by zero")


Calculator.zero(10, 100)
Calculator.zero(100, '100')
Calculator.zero(50, 'fifty')
Calculator.zero(0, 100)
