def func():
    repeating_values = [12,24,35,24,88,120,155,88,120,155]
    print(repeating_values)
    print(list(set(repeating_values))[::-1])
func()