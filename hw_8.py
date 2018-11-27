def create_dict(N):
    sqrt_dict = {i: i ** 2 for i in range(1, N + 1)}
    return sqrt_dict


print(create_dict(20))
print(create_dict(40))
print(create_dict(100))