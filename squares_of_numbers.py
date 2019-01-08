"""
Calculate squares of numbers

You have a list of numbers from 0 to 100000000000:
0, 1, 2, …, 99999999999

Please create a new list with squares of numbers from previous list.
Your new list should looks like:
0*0, 1*1, 2*2, 3*3, 4*4, …,  99999999999*99999999999

Please print values from the second list.

P.S. This task might look super easy, but there are a few cases. I guess, 
you’ll find them very quickly.
Your code should be able to execute on very simple computer(without huge 
amount of virtual memory, CPU, etc.)
Your code should works under both versions of Python (2.X, 3.X)

"""


def z_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


def squares_of_numbers():
    new_squares_list = (i * i for i in z_range(100000000000))
    for squared in new_squares_list:
        print(squared)


squares_of_numbers()
