"""
Calculate sum of all digits of a number set in string.

Example:

num = С12345Т

Your script should calculate it like: 1+2+3+4+5 = 15

num = С611091234512Т
result = 6+1+1+0+9+1+2+3+4+6+1+2 = 36
"""
def sum_str(n):
    sum_line = 0
    for i in n:
        sum_line += int(i)
    print("—ума строки {n} = {sum_line}".format(n=n,sum_line=sum_line) )

first_example = "93134053241522520541"
second_example = "6141232523952344"
third_example = "987654321123456789"
sum_str(first_example)
sum_str(second_example)
sum_str(third_example)