def my_func(a, b, c):
    arr = [a, b, c]
    small = min(arr)
    arr.remove(small)
    return sum(arr)


a, b, c = list(map(int, input('input a b c ').split()))

print(my_func(a, b, c))
