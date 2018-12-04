"""
Write a function which returns a dictionary with the following format:
return_square_dict(N)

{1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, …, N:N^2}
"""


def return_square_dict(N):
    return {i: i ** 2 for i in range(1, N + 1)}


print(return_square_dict(20))
print(return_square_dict(100))
