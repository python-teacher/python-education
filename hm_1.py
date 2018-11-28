"""
Calculate sum of all digits of a number set in string.

Example:

num = ‘12345’

Your script should calculate it like: 1+2+3+4+5 = 15

num = ‘611091234512’
result = 6+1+1+0+9+1+2+3+4+6+1+2 = 36
"""


def sum_str(n):
    sum_line = sum(int(i) for i in str(n) if i.isdigit())
    return ("Suma '{}' = {}".format(n,sum_line))


first_example = "931340532415225205491"
second_example = "61412325234952344"
third_example = "987654321123456789"
fourth_example = "999F9999saq999X91QBF"
print(sum_str(first_example))
print(sum_str(second_example))
print(sum_str(third_example))
print(sum_str(fourth_example))