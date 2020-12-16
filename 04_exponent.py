def my_func(x, y):
    key_number = 1
    if y < 0:
        for i in range(abs(y)):
            key_number *= 1 / x
    elif y > 0:
        for i in range(abs(y)):
            key_number *= x
    elif y == 0:
        return 1
    return key_number


x = int(input('Введите число '))
y = int(input('Введите степень '))

print(f'{my_func(x, y)}')
