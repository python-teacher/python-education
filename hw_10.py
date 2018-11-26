class calc:
    while True:
        try:
            a = int(input('a = '))
            b = int(input('b = '))
            sum = a / b
            print(sum)
        except (ZeroDivisionError, ValueError):
            print(False)
