def my_func(a):
    z = sum(a)
    return z


arr = []

while True:
    try:
        a = list(map(int, input('Введите строку чисел, разделенных пробелом, сумму которых необходимо найти ').split()))
        my_func(a)
        if a == str("exit"):
            break
        arr.append(my_func(a))
        print(sum(arr))
    except:
        print(sum(arr))
        break
