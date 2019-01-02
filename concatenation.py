"""
Calculate squares of numbers

You have a list of numbers from 0 to 100000000000:
0, 1, 2, �, 99999999999

Please create a new list with squares of numbers from previous list.
Your new list should looks like:
00, 11, 22, 33, 44, �, 9999999999999999999999

Please print values from the second list.

P.S. This task might look super easy, but there are a few cases. 
I guess, you�ll find them very quickly.
Your code should be able to execute on very simple computer(without 
huge amount of virtual memory, CPU, etc.)
Your code should works under both versions of Python (2.X, 3.X)
"""


def concatenation_of_two_numbers():
    mas_list = (x for x in range(0, 100000000000))
    new_mas_list = []
    for i in mas_list:
        concatenation = str(i) + str(i)
        print(concatenation)
        new_mas_list.append(concatenation)


concatenation_of_two_numbers()
